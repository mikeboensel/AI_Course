# JS to run on the "Manage Attendees" page of a Meetup event
#  attendees_dom= document.querySelectorAll('button[data-event-label="attendee-card"')

#  var attendees_fullnames = [];
# for(i of attendees_dom){
#  attendees_fullnames.push((i.querySelector('p')).textContent);
# }

# Populates the following array, we then break out first/last names via Python

with open("names.txt", "r") as file:
    attendees_fullnames = [line.strip() for line in file]


# for i in attendees:
#     print(i.split(" ")[0])

# First Names
print("First Names:")
for i in attendees_fullnames:
    print(" ".join(i.split(" ")[0:1]))

print("\n*************************")

print("Last Names:")
for i in attendees_fullnames:
    print(" ".join(i.split(" ")[1:]))
