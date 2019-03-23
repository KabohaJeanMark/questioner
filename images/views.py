from django.contrib.auth.models import User
from django.db.models import ProtectedError, Q
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer, ImageSerializerClass
from meetup.serializers import MeetingSerializer
from meetup.models import Meeting


class ImageList(APIView):
    """
    post:
    Create an image
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializerClass

    @classmethod
    @swagger_auto_schema(
        operation_description="Create an image for a specific meetup.",
        operation_id="Create image for a specific meetup",
        request_body=ImageSerializer,
        responses={
            201: ImageSerializer(many=False),
            400: "Invalid Format Data",
            401: "Unauthorized Access",
        },
    )
    def post(self, request, meetup_id):
        """
        post:
        Create a image for a specific meetup."
        """

        meeting = Meeting.objects.filter(id=meetup_id).first()
        if meeting:
            current_user = request.user
            if not current_user.is_superuser:
                return Response(
                    data={
                        "error": "Not authorized. Only admin has access",
                        "status": 401,
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            data = {}
            for key in request.data:
                data[key] = request.data[key]
            data["meetup_id"] = meetup_id
            data["created_by"] = request.user.id
            Mserializer = MeetingSerializer(meeting, many=False)

            serializer = ImageSerializer(data=data)
            if serializer.is_valid():

                serializer.save()
                image_dict = dict(serializer.data)
                del image_dict["meetup_id"]
                image_dict["created_by"] = current_user.username
                image_dict["meetup"] = Mserializer.data["title"]
                return Response(
                    data={
                        "status": status.HTTP_201_CREATED,
                        "data": [
                            {
                                "image": image_dict,
                                "success": "Image successfully added to meetup",
                            }
                        ],
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"error": "invalid meetup id"}, status=status.HTTP_400_BAD_REQUEST
        )
