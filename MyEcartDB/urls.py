from django.urls import path
from .views import  getCategorysDetails, getCategorysDetailsForID, getProductDetails, getProductDetailsForID, getSpecialOffersDetails,getCategorysDetailsForQUery

urlpatterns = [
    # path('login/', userLogin, name='user-login'),
    # path('signup/', userSignup, name='user-signup'),
    path('productDetails',getProductDetails, name='productDetails'),
    path('productDetails/<str:productID>',getProductDetailsForID, name='productDetailsForID'),
    path('categoryDetails',getCategorysDetails, name='categoryDetails'),
    path('categoryDetails/<str:categoryID>',getCategorysDetailsForID, name='categoryDetailsForID'),
    path('specialOfferDetails',getSpecialOffersDetails, name='specialOfferDetails'),
    # path('subscriptionplandetail/<str:susbscriptionID>',getSubscriptionPlanDetailsForID, name='subscriptionPlanDetailForID'),
    # path('usersubcribed/<str:susbscriptionID>',userSubcribed, name="userSubscribed"),
    # path('user',getUserSubscriptions, name='subscriptionPlanDetailForuserID')
]