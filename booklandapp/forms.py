from django import forms
import cloudinary.uploader
from .models import (
    AdmissionMessage,
    EnquiryMessages,
    TestimonialsMessage,
    LeadershipMessage,
    AlumniMessage,
    GalleryImage,
    FeaturedEvent,
    FeeStructure,
)


# =========================
# Admission Form
# =========================
class AdmissionMessageForm(forms.ModelForm):
    class Meta:
        model = AdmissionMessage
        fields = ["name", "email", "phone", "message"]


# =========================
# Enquiry Form
# =========================
class EnquiryMessagesForm(forms.ModelForm):
    class Meta:
        model = EnquiryMessages
        fields = ["name", "email", "subject", "message"]


# =========================
# Testimonials Form
# =========================
class TestimonialsMessageForm(forms.ModelForm):
    upload_image = forms.ImageField(required=False, label="Upload Image")

    class Meta:
        model = TestimonialsMessage
        fields = ["name", "title", "testimonial", "upload_image"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get("upload_image")
        if image_file:
            upload_result = cloudinary.uploader.upload(
                image_file,
                folder="bookland/testimonials",
                quality="auto",
                fetch_format="auto",
            )
            instance.image = upload_result.get("secure_url")
        if commit:
            instance.save()
        return instance


# =========================
# Leadership Form
# =========================
class LeadershipMessageForm(forms.ModelForm):
    upload_image = forms.ImageField(required=False, label="Upload Image")

    class Meta:
        model = LeadershipMessage
        fields = ["salutation", "name", "designation", "message", "upload_image"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get("upload_image")
        if image_file:
            upload_result = cloudinary.uploader.upload(
                image_file,
                folder="bookland/leadership",
                quality="auto",
                fetch_format="auto",
            )
            instance.image = upload_result.get("secure_url")
        if commit:
            instance.save()
        return instance


# =========================
# Alumni Form
# =========================
class AlumniMessageForm(forms.ModelForm):
    upload_image = forms.ImageField(required=False, label="Upload Image")

    class Meta:
        model = AlumniMessage
        fields = ["name", "title", "year_of_completion", "message", "upload_image"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get("upload_image")
        if image_file:
            upload_result = cloudinary.uploader.upload(
                image_file,
                folder="bookland/alumni",
                quality="auto",
                fetch_format="auto",
            )
            instance.image = upload_result.get("secure_url")
        if commit:
            instance.save()
        return instance


# =========================
# Gallery Image Form
# =========================
class GalleryImageForm(forms.ModelForm):
    upload_image = forms.ImageField(required=True, label="Upload Image")

    class Meta:
        model = GalleryImage
        fields = ["title", "upload_image"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get("upload_image")
        if image_file:
            upload_result = cloudinary.uploader.upload(
                image_file,
                folder="bookland/gallery",
                quality="auto",
                fetch_format="auto",
            )
            instance.image = upload_result.get("secure_url")
        if commit:
            instance.save()
        return instance


# =========================
# Featured Event Form
# =========================
class FeaturedEventForm(forms.ModelForm):
    upload_image = forms.ImageField(required=False, label="Upload Image")

    class Meta:
        model = FeaturedEvent
        fields = ["title", "start_date", "end_date", "description", "upload_image"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get("upload_image")
        if image_file:
            upload_result = cloudinary.uploader.upload(
                image_file,
                folder="bookland/featured_events",
                quality="auto",
                fetch_format="auto",
            )
            instance.image = upload_result.get("secure_url")
        if commit:
            instance.save()
        return instance


# =========================
# Fee Structure Form
# =========================
class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = [
            "level",
            "tuition_per_term",
            "meals_fee",
            "transport_fee",
            "fee_structure_file",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fee_structure_file'].help_text = (
            "Upload PDF file (max 10MB). This file will be public via Cloudinary."
        )
