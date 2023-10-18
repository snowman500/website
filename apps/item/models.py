# bom models
from extensions.models import *
from extensions.common.base_model import *
from django.core.validators import MaxValueValidator, MinValueValidator



class WarehouseInfo(BaseModel):
    """仓库信息表"""
    warehouse_code = CharField(max_length=50, default='001', verbose_name='仓库编码')
    warehouse_name = CharField(max_length=50, default='深圳仓库', verbose_name='仓库名称')
    link_man = CharField(max_length=256, default='王八一', verbose_name='仓库联系人')
    phone_number = CharField(max_length=50, default='15892564569', verbose_name='仓库联系人电话')
    province = CharField(max_length=50, default='广东省', verbose_name='省')
    city = CharField(max_length=50, default='深圳市', verbose_name='市')
    distrct = CharField(max_length=50, default='光明区', verbose_name='区')
    address = CharField(max_length=50, default='公明街道丽水湖畔105号', verbose_name='仓库地址')
#   team = ForeignKey('system.Team', on_delete=CASCADE, related_name='warehouse_info')

    class Meta:
        db_table = 'item_warehouse_info' # 定义属性表名字
        verbose_name = '仓库信息表'
        verbose_name_plural = verbose_name
        

class ShippingInfo(BaseModel):
    """物流公司信息表"""
    ship_name = CharField(max_length=50, verbose_name='物流公司名称')
    link_man = CharField(max_length=256, verbose_name='物流公司联系人')
    phone_number = CharField(max_length=50, verbose_name='物流公司联系人电话')
    price  = CharField(max_length=50, verbose_name='价格')

    class Meta:
        db_table = 'item_ShippingInfo' # 定义属性表名字
        verbose_name = '物流公司信息表'
        verbose_name_plural = verbose_name


class Supplier(BaseModel):
    """供应商信息表"""
    supplier_code = CharField(max_length=10, default='JF0000', verbose_name='启用状态')
    supplier_name = CharField(max_length=50, default='深圳市有限公司', verbose_name='供应商名称')
    link_man = CharField(max_length=256, default='胡八一', verbose_name='联系人')
    phone_number = CharField(max_length=50, default='13566200014',  verbose_name='联系人电话')
    bank_name = CharField(max_length=50, default='中国银行深圳分行',  verbose_name='供应商开户银行名称')
    bank_account = CharField(max_length=50, default='6226097558970588',  verbose_name='银行账号')
    address = CharField(max_length=50, default='广东省深圳市宝安区石岩街道65号',  verbose_name='供应商地址')
#    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='supplier')
    
    """ 定义了一个save的方法,用于保存模型实例。当保存新的供应商时，
    这个方法会检查是否存在已有的供应商编码。如果存在，则会将新的供应商编码设置为上一个供应商编码加1。
    如果不存在，则会将新的供应商编码设置为"JF0001" """

    def save(self, *args, **kwargs):
        if not self.pk:
            last_supplier = Supplier.objects.all().order_by('id').last()
            if last_supplier:
                last_code = last_supplier.supplier_code
                new_code = 'JF' + str(int(last_code[2:]) + 1).zfill(4)
                self.supplier_code = new_code
        super(Supplier, self).save(*args, **kwargs)


    class Meta:
        db_table = 'item_supplier' # 定义属性表名字
        verbose_name = '供应商信息表'
        verbose_name_plural = verbose_name


# Create your models here.
class ItemCategory(BaseModel):
    """物料类别"""
    # 一级: 0-9
    # 二级--四级: 00-99
    item_id = CharField(max_length=2, default='1', verbose_name='类别分类代码')
    item = CharField(max_length=10, default='采购', verbose_name='类别名称') 
    parent = ForeignKey('self', null=True, blank=True, on_delete=CASCADE, related_name='item_category', verbose_name='父类别')
#    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='item_category')
    class Meta:
        db_table = 'item_category'
        verbose_name = '物料类别'
        verbose_name_plural = verbose_name


class ItemSpecification(BaseModel):
    """物料属性表"""
    name = CharField(max_length=10, default='PCB属性', verbose_name='物料类属性')
    name_id = CharField(max_length=10, default='1.5.03.01', verbose_name='四级物料代码')
    remark = CharField(max_length=256, default='关于啥啥啥的属性,和啥啥啥不一样', null=True, blank=True, verbose_name='备注')
    spec_1 = CharField(max_length=64, default='属性', verbose_name='自定义规格1')
    spec_2 = CharField(max_length=64, default='属性', verbose_name='自定义规格2')
    spec_3 = CharField(max_length=64, default='属性', verbose_name='自定义规格3')
    spec_4 = CharField(max_length=64, default='属性', verbose_name='自定义规格4')
    spec_5 = CharField(max_length=64, default='属性', verbose_name='自定义规格5')
    spec_6 = CharField(max_length=64, default='属性', verbose_name='自定义规格6')
    spec_7 = CharField(max_length=64, default='属性', verbose_name='自定义规格7')
    spec_8 = CharField(max_length=64, default='属性', verbose_name='自定义规格8')
    spec_9 = CharField(max_length=64, default='属性', verbose_name='自定义规格9')
    spec_10 = CharField(max_length=64, default='属性', verbose_name='自定义规格10')



    class Meta:
        db_table = 'item_item_specification'
        verbose_name = '物料属性表'
        verbose_name_plural = verbose_name


class ItemUnit(Model):
    """产品单位"""
    name = CharField(max_length=64, verbose_name='名称')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')

    class Meta:
        db_table = 'item_unit'
        verbose_name = '产品单位表'
        verbose_name_plural = verbose_name


class ItemSKU(BaseModel):
    '''物料表'''
    spec = ForeignKey(ItemSpecification, on_delete=PROTECT,verbose_name='属性类目', related_name='itemsku_itemspecification')
    supplier = ForeignKey(Supplier, on_delete=PROTECT,verbose_name='供应商名称', related_name='itemsku_itemsupplier') # 供应商外键
    is_launched = BooleanField(default=True, verbose_name='是否上架销售') # 默认上架
    goods =CharField(max_length=64, verbose_name='物料型号:JF-D-002')  # 
    item_id = CharField(max_length=20, verbose_name='物料编码:F2.2.09.30.00000')    
    name = CharField(max_length=20, verbose_name='物料名称')
    desc = CharField(max_length=256, verbose_name='物料简介')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='物料价格')
    unite = CharField(max_length=20, verbose_name='物料单位')
    w_id = ForeignKey('WarehouseInfo', on_delete=PROTECT,verbose_name='仓库ID', related_name='warehouse_item')
    current_cnt = CharField(max_length=256, verbose_name='库存数量')
    lock_cnt = CharField(max_length=50, verbose_name='锁库数量')
    in_transit_cnt = CharField(max_length=50, verbose_name='在途数量')
    sales = ForeignKey(Supplier, on_delete=PROTECT, verbose_name='物料销量', related_name='sku_supplier')
    #team = ForeignKey('system.Team', on_delete=CASCADE, related_name='item_sku')
    
    @classmethod
    def get_number(cls, team):
        default_number = 'F2.2.09.30.00000'
        if instance := cls.objects.filter(team=team).last():
            if result := re.findall('[0-9]+', instance.number):
                current_number = result[-1]
                next_number = str(int(current_number) + 1)

                if len(current_number) > len(next_number):
                    next_number = next_number.zfill(len(current_number))
            else:
                return default_number
        else:
            return default_number
        
        result = re.match(f'^(.*){current_number}(.*?)$', instance.number)
        prefix, suffix = result.group(1), result.group(2)

        return prefix + next_number + suffix
    
    class Meta:
        unique_together = [('item_id')]
        db_table = 'item_sku'
        verbose_name = '物料表'
        verbose_name_plural = verbose_name
