from django.http import JsonResponse

from .models import Conference, Location


def api_list_conferences(request):
    """
    Lists the conference names and the link to the conference.

    Returns a dictionary with a single key "conferences" which
    is a list of conference names and URLS. Each entry in the list
    is a dictionary that contains the name of the conference and
    the link to the conference's information.

    {
        "conferences": [
            {
                "name": conference's name,
                "href": URL to the conference,
            },
            ...
        ]
    }
    """
    response = []
    conferences = Conference.objects.all()
    for conference in conferences:
        response.append(
            {
                "name": conference.name,
                "href": conference.get_api_url(),
            }
        )
    return JsonResponse({"conferences": response})


def api_show_conference(request, pk):
    """
    Returns the details for the Conference model specified
    by the pk parameter.

    This should return a dictionary with the name, starts,
    ends, description, created, updated, max_presentations,
    max_attendees, and a dictionary for the location containing
    its name and href.

    {
        "name": the conference's name,
        "starts": the date/time when the conference starts,
        "ends": the date/time when the conference ends,
        "description": the description of the conference,
        "created": the date/time when the record was created,
        "updated": the date/time when the record was updated,
        "max_presentations": the maximum number of presentations,
        "max_attendees": the maximum number of attendees,
        "location": {
            "name": the name of the location,
            "href": the URL for the location,
        }
    }
    """
    conference = Conference.objects.get(id=pk)
    return JsonResponse(
        {
            "name": conference.name,
            "starts": conference.starts,
            "ends": conference.ends,
            "description": conference.description,
            "created": conference.created,
            "updated": conference.updated,
            "max_presentations": conference.max_presentations,
            "max_attendees": conference.max_attendees,
            "location": {
                "name": conference.location.name,
                "href": conference.location.get_api_url(),
            },
        }
    )


def api_list_locations(request):
    """
    Lists the location names and the link to the location.

    Returns a dictionary with a single key "locations" which
    is a list of location names and URLS. Each entry in the list
    is a dictionary that contains the name of the location and
    the link to the location's information.

    {
        "locations": [
            {
                "name": location's name,
                "href": URL to the location,
            },
            ...
        ]
    }
    """
    response = []
    locations = Location.objects.all()
    for location in locations:
        response.append(
            {
                "name": location.name,
                "href": location.get_api_url(),
            }
        )
    return JsonResponse({"locations": response})


def api_show_location(request, pk):
    """
    Returns the details for the Location model specified
    by the pk parameter.

    This should return a dictionary with the name, city,
    room count, created, updated, and state abbreviation.

    {
        "name": location's name,
        "city": location's city,
        "room_count": the number of rooms available,
        "created": the date/time when the record was created,
        "updated": the date/time when the record was updated,
        "state": the two-letter abbreviation for the state,
    }
    """

    # name = models.CharField(max_length=200)
    # city = models.CharField(max_length=200)
    # room_count = models.PositiveSmallIntegerField()
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    # state = models.ForeignKey(
    #     State,
    #     related_name="+",  # do not create a related name on State
    #     on_delete=models.PROTECT,
    # )
    location = Location.objects.get(id=pk)
    return JsonResponse(
        {
            "name": location.name,
            "city": location.city,
            "room_count": location.room_count,
            "created": location.created,
            "updated": location.updated,
            "state": {
                "name": location.state.name,
                "abbreviation": location.state.abbreviation,
            },
        }
    )
