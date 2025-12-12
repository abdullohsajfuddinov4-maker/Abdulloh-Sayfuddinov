from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Nomi juda qisqa (min. 3 harf)")
        return name
    '''
    def clean_category(self):
        category = self.cleaned_data['category']
        if not category or len(category.name) < 3:
            raise forms.ValidationError("Kategoriya nomi juda qisqa (min. 3 harf)")
        return category
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 100:
            raise forms.ValidationError("Narx juda past (min. 100 so'm)")
        return price
        

    def clean_country(self):
        country = self.cleaned_data['country']
        if len(country) < 3:
            raise forms.ValidationError("Mamlakat nomi juda qisqa (min. 3 harf)")
        return country

    def clean_brand(self):
        brand = self.cleaned_data['brand']
        if len(brand) < 3:
            raise forms.ValidationError("Brend nomi juda qisqa (min. 3 harf)")
        return brand

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight > 25:
            raise forms.ValidationError("Og'irlik 25 kg dan oshmasligi kerak")
        return weight

    def clean_color(self):
        color = self.cleaned_data['color']
        if len(color) < 3:
            raise forms.ValidationError("Rang nomi juda qisqa (min. 3 harf)")
        return color

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) < 10:
            raise forms.ValidationError("Tavsif juda qisqa (min. 10 harf)")
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            extension = image.name.split('.')[-1].lower()
            allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
            if extension not in allowed_extensions:
                raise forms.ValidationError(
                    "Faqat rasm fayllari ruxsat etiladi: jpg, jpeg, png, gif"
                )
        return image

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("Ombor miqdor nolga teng yoki undan katta bo'lishi kerak")
        return stock
'''
