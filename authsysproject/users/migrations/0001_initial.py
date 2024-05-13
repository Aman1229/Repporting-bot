# Generated by Django 5.0.1 on 2024-02-27 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AudiometryReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='uploads/audiometry_pdfs/')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('patient_id', models.CharField(blank=True, max_length=20, null=True)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('report_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='audioPatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientId', models.CharField(max_length=15)),
                ('PatientName', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=15)),
                ('TestDate', models.CharField(max_length=20)),
                ('ReportDate', models.CharField(max_length=20)),
                ('rightEarDB', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('leftEarDB', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('rightEarBoneDB', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('leftEarBoneDB', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('rightEarLevel', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('leftEarLevel', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=25)),
                ('acnumber', models.CharField(max_length=15)),
                ('ifsc', models.CharField(max_length=15)),
                ('pancardno', models.CharField(max_length=15)),
                ('pandcard', models.FileField(upload_to='uploads/')),
                ('cheque', models.FileField(upload_to='uploads/')),
                ('pictureproof', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EcgReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='uploads/ecg_pdfs/')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('patient_id', models.CharField(blank=True, max_length=20, null=True)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('report_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionModalities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mriopt1', models.CharField(max_length=100)),
                ('mriothers1', models.CharField(max_length=100)),
                ('ctopt1', models.CharField(max_length=100)),
                ('ctothers1', models.CharField(max_length=100)),
                ('xray1', models.BooleanField()),
                ('others1', models.BooleanField()),
                ('rdoprefrence', models.CharField(max_length=15)),
                ('exnocase', models.IntegerField()),
                ('urgent', models.CharField(max_length=30)),
                ('nonurgent', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OptometryReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='uploads/optometry_pdfs/')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('patient_id', models.CharField(blank=True, max_length=20, null=True)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('report_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='optopatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientId', models.CharField(max_length=50)),
                ('PatientName', models.CharField(max_length=70)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('TestDate', models.CharField(max_length=50)),
                ('ReportDate', models.CharField(max_length=50)),
                ('FarVisionRight', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('FarVisionLeft', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('NearVisionRight', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('NearVisionLeft', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('ColorBlindness', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientId', models.CharField(max_length=50)),
                ('PatientName', models.CharField(max_length=70)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('TestDate', models.CharField(max_length=50)),
                ('ReportDate', models.CharField(max_length=50)),
                ('height', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('weight', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('blood', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pulse', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('FarVisionRight', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('FarVisionLeft', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('NearVisionRight', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('NearVisionLeft', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('ColorBlindness', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QualificationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tensname', models.CharField(max_length=30)),
                ('tengrade', models.CharField(max_length=10)),
                ('tenpsyr', models.CharField(max_length=15)),
                ('tencertificate', models.FileField(upload_to='uploads/')),
                ('twelvesname', models.CharField(max_length=30)),
                ('twelvegrade', models.CharField(max_length=10)),
                ('twelvepsyr', models.CharField(max_length=15)),
                ('twelvecertificate', models.FileField(upload_to='uploads/')),
                ('mbbsinstitution', models.CharField(max_length=25)),
                ('mbbsgrade', models.CharField(max_length=10)),
                ('mbbspsyr', models.CharField(max_length=10)),
                ('mbbsmarksheet', models.FileField(upload_to='uploads/')),
                ('mbbsdegree', models.FileField(upload_to='uploads/')),
                ('mdinstitution', models.CharField(max_length=25)),
                ('mdgrade', models.CharField(max_length=10)),
                ('mdpsyr', models.CharField(max_length=10)),
                ('mddegree', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='ReportingArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mriopt', models.CharField(max_length=100)),
                ('mriothers', models.CharField(max_length=100)),
                ('ctopt', models.CharField(max_length=100)),
                ('ctothers', models.CharField(max_length=100)),
                ('xray', models.BooleanField()),
                ('others', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='TimeAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('sunday', models.BooleanField()),
                ('monst', models.CharField(default='Individual', max_length=255)),
                ('monend', models.CharField(default='Individual', max_length=255)),
                ('tuest', models.CharField(default='Individual', max_length=255)),
                ('tueend', models.CharField(default='Individual', max_length=255)),
                ('wedst', models.CharField(default='Individual', max_length=255)),
                ('wedend', models.CharField(default='Individual', max_length=255)),
                ('thust', models.CharField(default='Individual', max_length=255)),
                ('thuend', models.CharField(default='Individual', max_length=255)),
                ('frist', models.CharField(default='Individual', max_length=255)),
                ('friend', models.CharField(default='Individual', max_length=255)),
                ('satst', models.CharField(default='Individual', max_length=255)),
                ('satend', models.CharField(default='Individual', max_length=255)),
                ('sunst', models.CharField(default='Individual', max_length=255)),
                ('sunend', models.CharField(default='Individual', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Total_Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_uploaded_xray', models.IntegerField(default=0)),
                ('total_uploaded_ecg', models.IntegerField(default=0)),
                ('total_reported_xray', models.IntegerField(default=0)),
                ('total_reported_ecg', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='vitalPatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientId', models.CharField(max_length=50)),
                ('PatientName', models.CharField(max_length=70)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('TestDate', models.CharField(max_length=50)),
                ('ReportDate', models.CharField(max_length=50)),
                ('height', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('weight', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('blood', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pulse', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VitalsReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='uploads/vitals_pdfs/')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('patient_id', models.CharField(blank=True, max_length=20, null=True)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('report_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='XClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='XrayReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='uploads/xray_pdfs/')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('patient_id', models.CharField(blank=True, max_length=20, null=True)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('report_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.client')),
            ],
        ),
        migrations.CreateModel(
            name='InstPersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instadd', models.CharField(max_length=100)),
                ('cnprname', models.CharField(max_length=30)),
                ('cnprdesignation', models.CharField(max_length=25)),
                ('cnprphone', models.CharField(max_length=10)),
                ('altcnprname', models.CharField(max_length=30)),
                ('altcnprdesignation', models.CharField(max_length=25)),
                ('altcnprphone', models.CharField(max_length=10)),
                ('emailfraccount', models.EmailField(max_length=50)),
                ('accountcnpr', models.CharField(max_length=15)),
                ('acccnprphone', models.CharField(max_length=10)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('technician_name', models.CharField(default='Unknown Technician', max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.city')),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_field', models.DateField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.location')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnfpassword', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('altphone', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('reference', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('resume', models.FileField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('uploadpicture', models.FileField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('signature', models.FileField(blank=True, default=None, null=True, upload_to='media')),
                ('companylogo', models.FileField(blank=True, default=None, null=True, upload_to='media')),
                ('total_reported', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('serviceslist', models.ManyToManyField(to='users.serviceslist')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientId', models.CharField(max_length=50)),
                ('PatientName', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=15)),
                ('HeartRate', models.CharField(blank=True, max_length=30, null=True)),
                ('TestDate', models.CharField(max_length=20)),
                ('ReportDate', models.CharField(max_length=20)),
                ('PRInterval', models.CharField(blank=True, max_length=30, null=True)),
                ('reportimage', models.URLField(blank=True, null=True)),
                ('isDone', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('date', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.date')),
                ('cardiologist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exinstitution', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('exstdate', models.DateField(blank=True, default=None, null=True)),
                ('exenddate', models.DateField(blank=True, default=None, null=True)),
                ('designation', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('exinstitution1', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('exstdate1', models.DateField(blank=True, default=None, null=True)),
                ('exenddate1', models.DateField(blank=True, default=None, null=True)),
                ('designation1', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('prexst', models.DateField(blank=True, default=None, null=True)),
                ('prexend', models.DateField(blank=True, default=None, null=True)),
                ('pii', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('msname', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('mcirgno', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('regcecr', models.FileField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='XCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.xclient')),
            ],
        ),
        migrations.CreateModel(
            name='XLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.xcity')),
            ],
        ),
        migrations.CreateModel(
            name='DICOMData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, max_length=50)),
                ('patient_id', models.CharField(blank=True, max_length=20)),
                ('age', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('study_date', models.CharField(blank=True, max_length=50)),
                ('study_description', models.CharField(blank=True, max_length=100)),
                ('dicom_file', models.FileField(upload_to='uploads/')),
                ('jpeg_file', models.ImageField(upload_to='uploads/')),
                ('isDone', models.BooleanField(default=False)),
                ('notes', models.CharField(default=True, max_length=50000)),
                ('total_cases', models.IntegerField(blank=True, default=None, null=True)),
                ('radiologist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.personalinfo')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.xlocation')),
            ],
        ),
    ]
