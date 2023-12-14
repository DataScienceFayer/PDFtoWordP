from django.db import models

class ConvertedFile(models.Model):
    pdf_file = models.FileField(upload_to='pdf_files/')
    docx_file = models.FileField(upload_to='docx_files/')
    converted_at = models.DateTimeField(auto_now_add=True)
    short_code = models.CharField(max_length=10, unique=True, null=True,blank=True)

    def __str__(self):
        return f"{self.pdf_file.name} - {self.converted_at}"
