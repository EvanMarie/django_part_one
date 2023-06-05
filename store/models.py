from django.db import models


# Product to Promotion: a promotion can apply to multiple products,
# and a product can have multiple promotions
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # all the products this promotion applies to


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    # This makes the sku the primary key/unique id and Django will not create an id field
    # sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # if a collection is deleted, PROTECT will prevent the deletion of the products within
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    # Creating a variable for the default membership to simplify any changes in the future
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    # Creating a list of tuples for the membership choices
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    given_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True)
    # Choice field - https://docs.djangoproject.com/en/3.2/ref/models/fields/#choices
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    class Meta:
        # creating indexes for last_name and first_name.
        # Indexes are used to speed up queries
        indexes = [
            models.Index(fields=['last_name', 'given_name']),
        ]


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    # auto_now_add - the first time the object is created, set the value to the current
    # date/time
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    # if a customer is deleted, PROTECT will prevent the deletion of the orders within
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    # if an order is deleted, PROTECT will prevent the deletion of the order items within
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    # if a product is deleted, PROTECT will prevent the deletion of the order items within
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    # product prices can change. This stores the price at the time of the order
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


# one-to-one relationship between customers and addresses
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10, default='00000')
    # if the customer to address is one-to-one, i.e. they can have one address
    # customer = models.OneToOneField(
    #     Customer, on_delete=models.CASCADE, primary_key=True)
    # to allow customers more than one address: One-to-many relationship
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    # if a cart is deleted, all items within will be deleted as well
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # if a product is deleted, it will be deleted from all shopping carts as well
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
