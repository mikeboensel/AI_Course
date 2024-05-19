#  attendees= document.querySelectorAll('button[data-event-label="attendee-card"')

#  var a = [];
# for(i of attendees){
#  a.push((i.querySelector('span')).textContent);
# }
attendees = [
    "Michael Boensel",
    "Suprateem Banerjee",
    "Erik Pohl",
    "Mark Sabalauskas",
    "Kien Lang",
    "XingxingShang",
    "Dan Petrie",
    "Dimitris Tselios",
    "Steve Bernard",
    "Martin Bakal",
    "Richard Torres",
    "Madhavan Munisamy",
    "Kris Nybakken",
    "Vishal Panchamia",
    "Te Chen Chiu",
    "Evelina Averin",
    "Will Dzierson",
    "Dimo Babenco",
    "Travis  McGee",
    "Sanchit Dass",
    "Makarand Zende",
    "Will Sergeant",
    "Curt CurtR",
    "Roys Güreli",
    "Aleef Mahmud",
    "Sridharan Gopal",
    "Robert Zacharski",
    "Fabio Lopez",
    "Ramy Solanki",
    "Justin Ho",
    "Mileva Van Tuyl",
    "casey dimascio",
    "Uma Mahesh",
    "Aditya Ponnada",
    "Marianna Nakos",
    "Thomas DeMeo",
    "Sarath Chandra Oruganti",
    "Daniel Vent",
    "Connor Fitzgerald",
    "Winston Li",
    "Tejaswini Tanaji Chavan",
    "Tianfang Xie",
    "mohit manjaria",
    "Leena Doultani ",
    "yimei wen",
    "saurabh shetty",
    "Aditya Singh",
    "Tae Hyun Kim",
    "Adriana Beltran Andrade",
    "Sergei Gourski",
    "Yury Alkhazov",
    "Kevin McElroy",
]

# for i in attendees:
#     print(i.split(" ")[0])

for i in attendees:
    print(" ".join(i.split(" ")[1:]))
