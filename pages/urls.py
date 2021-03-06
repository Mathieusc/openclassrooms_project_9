from django.urls import path

from .views import (
    home_page_view,
    TicketDetailView,
    ReviewDetailView,
    TicketCreateView,
    review_response,
    ReviewCreateView,
    TicketUpdateView,
    ReviewUpdateView,
    TicketDeleteView,
    ReviewDeleteView,
    Posts,
    subscribers,
    unsubscribe,
)

urlpatterns = [
    path("", home_page_view, name="home"),
    path("ticket/<int:pk>/", TicketDetailView.as_view(), name="ticket-detail"),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
    path("ticket/new/", TicketCreateView.as_view(), name="ticket-create"),
    path("ticket/<int:ticket_id>/response/", review_response, name="review-response"),
    path("review/new/", ReviewCreateView.as_view(), name="review-create"),
    path("ticket/<int:pk>/update/", TicketUpdateView.as_view(), name="ticket-update"),
    path("review/<int:pk>/update/", ReviewUpdateView.as_view(), name="review-update"),
    path("ticket/<int:pk>/delete/", TicketDeleteView.as_view(), name="ticket-delete"),
    path("review/<int:pk>/delete/", ReviewDeleteView.as_view(), name="review-delete"),
    path("posts/", Posts.as_view(), name="posts-users"),
    path("subscribers/", subscribers, name="subscribers"),
    path(
        "<int:followed_by_id><int:following_id>/unsubscribe/",
        unsubscribe,
        name="unsubscribe",
    ),
]
