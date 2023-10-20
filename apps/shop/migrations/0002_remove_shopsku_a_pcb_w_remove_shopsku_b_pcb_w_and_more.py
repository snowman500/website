# Generated by Django 4.2.6 on 2023-10-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopsku',
            name='a_pcb_w',
        ),
        migrations.RemoveField(
            model_name='shopsku',
            name='b_pcb_w',
        ),
        migrations.RemoveField(
            model_name='shopsku',
            name='c_pcb_w',
        ),
        migrations.RemoveField(
            model_name='shopsku',
            name='d_pcb_w',
        ),
        migrations.AddField(
            model_name='shopsku',
            name='pcb_w',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='PCB宽度'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='a_cnt',
            field=models.CharField(max_length=16, verbose_name='连接器1'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='b_cnt',
            field=models.CharField(max_length=16, verbose_name='连接器2'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='c_cnt',
            field=models.CharField(max_length=16, verbose_name='连接器3'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='d_cnt',
            field=models.CharField(max_length=16, verbose_name='连接器4'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='主图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image10',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='image9',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图'),
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='lens',
            field=models.CharField(max_length=16, verbose_name='透镜类型'),
        ),
    ]
