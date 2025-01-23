# JS to run on the "Manage Attendees" page of a Meetup event
#  attendees_dom= document.querySelectorAll('button[data-event-label="attendee-card"')

#  var attendees_fullnames = [];
# for(i of attendees_dom){
#  attendees_fullnames.push((i.querySelector('p')).textContent);
# }

# Populates the following array, we then break out first/last names via Python

attendees_fullnames = [
    "Michael Boensel",
    "Subham Swastik",
    "Chris Rappoli",
    "Andrew Ressler",
    "tommy williams",
    "Gabe Saxe",
    "Abby Damodaran",
    "arielle vargas",
    "Jeff Levetin",
    "Drew Nemer",
    "Ujwalw Wasekar",
    "Phillip Zhou",
    "Brad Kaufman",
    "Khush Patel",
    "Stefania Mitova",
    "Suprateem Banerjee",
    "Andy Braren",
    "Jason Stillerman",
    "Payal Nagaonkar",
    "Mahesh Kasana",
    "Cameron Fen",
    "Gabriel Leal",
    "Matt Carroll",
    "Ralph Baker",
    "Mel Fish",
    "Al Cole",
    "Besmira Elezi",
    "Fong Wis",
    "Quan Tran",
    "Senthil Palanivelu",
    "Altyn Murat",
    "Yuxiao Wang",
    "Sathwik Matcha",
    "Cooper Reed",
    "Lafcadio Flint",
    "Bhushan Suwal",
    "Jeffery Jacobs",
    "Nikhileshwar Reddy Bommareddy",
    "Arun Gona",
    "Nick Yee",
    "Sean Woodruff",
    "David González",
    "Zin Ma",
    "Chunyee Leung",
    "Takin Tadayon",
    "Zahra Naghdi",
    "Harshil Nandwani",
    "chaoyi jiang",
    "Naga harish k",
    "Rakesh Kumar",
    "Ari Roshko ",
    "Eric Mariasis",
    "Rajkumar Rajamanickam",
    "Carissa Lacson",
    "James Xue",
    "Mark Bluemer",
    "Srijha Kalyan",
    "Gbolahan Alli",
    "Piotr Cetner",
    "Siddarth Karuppusamy",
    "Craig Chamberlain",
    "Sankalpa Kattel",
    "Myo Thet Kyaw",
    "Bryan Sierra",
    "Padmaja Surendranath",
    "Jessica Mejia",
    "Harsha Sheshanna",
    "Arsen Avanesian",
    "Nithin Gowrav",
    "Jen Looper",
    "Jon Wolheim",
    "Prithvi Prakash",
    "Mahesh Acharya",
    "Kavach Shah",
    "Chirag Malhotra",
    "Hadi Khalaf",
    "Maggie Moran",
]

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
