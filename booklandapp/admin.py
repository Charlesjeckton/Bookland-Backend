from django.contrib import admin
from django.utils.html import format_html

from .models import (
    AdmissionMessage,
    EnquiryMessages,
    AlumniMessage,
    LeadershipMessage,
    TestimonialsMessage,
    FeeStructure,
    Event,
    FeaturedEvent,
    GalleryImage,
    KeyAdmissionDeadline,
)
from .forms import (
    TestimonialsMessageForm,
    LeadershipMessageForm,
    AlumniMessageForm,
    FeaturedEventForm,
    GalleryImageForm,
    FeeStructureForm,
)


# =====================================================
# Utility to display Cloudinary image previews
# =====================================================
def cloudinary_image_preview(obj, field_name="image"):
    url = getattr(obj, field_name, None)
    if url:
        return format_html(
            '<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 4px;" />',
            url
        )
    return "No Image"


cloudinary_image_preview.short_description = "Preview"


# =====================================================
# Generic Admin Mixin for Image Preview
# =====================================================
class ImagePreviewAdminMixin(admin.ModelAdmin):
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        return cloudinary_image_preview(obj)


# =====================================================
# Testimonials Admin
# =====================================================
@admin.register(TestimonialsMessage)
class TestimonialsMessageAdmin(ImagePreviewAdminMixin):
    form = TestimonialsMessageForm
    list_display = ("name", "title", "testimonial", "image_preview")


# =====================================================
# Leadership Admin
# =====================================================
@admin.register(LeadershipMessage)
class LeadershipMessageAdmin(ImagePreviewAdminMixin):
    form = LeadershipMessageForm
    list_display = ("salutation", "name", "designation", "message", "image_preview")


# =====================================================
# Alumni Admin
# =====================================================
@admin.register(AlumniMessage)
class AlumniMessageAdmin(ImagePreviewAdminMixin):
    form = AlumniMessageForm
    list_display = ("name", "title", "year_of_completion", "message", "image_preview")


# =====================================================
# Gallery Image Admin
# =====================================================
@admin.register(GalleryImage)
class GalleryImageAdmin(ImagePreviewAdminMixin):
    form = GalleryImageForm
    list_display = ("title", "image_preview")


# =====================================================
# Featured Event Admin
# =====================================================
@admin.register(FeaturedEvent)
class FeaturedEventAdmin(ImagePreviewAdminMixin):
    form = FeaturedEventForm
    list_display = ("title", "start_date", "end_date", "image_preview")


# =====================================================
# Fee Structure Admin (PDF download & preview)
# =====================================================
@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ("level", "tuition_per_term", "meals_fee", "transport_fee", "total_fee", "download_link")
    readonly_fields = ("download_link",)
    search_fields = ("level",)
    list_filter = ("level",)

    fieldsets = (
        ("Fee Information", {
            "fields": ("level", "tuition_per_term", "meals_fee", "transport_fee", "total_fee")
        }),
        ("PDF Document", {
            "fields": ("fee_structure_file", "download_link"),
            "description": "Upload PDF file (public). All PDFs will be publicly accessible."
        }),
    )

    def download_link(self, obj):
        if obj.fee_structure_file:
            return format_html(
                '<a href="{}" target="_blank" class="btn btn-primary btn-sm">'
                '⬇️ Download PDF</a>', obj.file_url
            )
        return "No PDF uploaded"

    download_link.short_description = "PDF Download"


# =====================================================
# Standard models (no images or PDFs, default admin)
# =====================================================
admin.site.register(AdmissionMessage)
admin.site.register(EnquiryMessages)
admin.site.register(Event)
admin.site.register(KeyAdmissionDeadline)
