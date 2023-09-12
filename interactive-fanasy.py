##!/usr/bin/env python3
import sys

world = {
  "uuid": "441AD245-291A-4F37-9326-652F6518621A",
  "name": "Run",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631484567185,
  "passages": [
    {
      "name": "Open Field",
      "tags": "",
      "id": "1",
      "text": "Scurring from your abandoned car on the bleak, shadowed interstate road, you make for the closest corn field to aid in your escape. You hear faint snarling in the distance.\n\n[[WEST->West Field]]\n[[EAST->East Field]]\n[[SOUTH->Abandoned Car]]\n[[NORTH->North Field]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West Field",
          "original": "[[WEST->West Field]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East Field",
          "original": "[[EAST->East Field]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Abandoned Car",
          "original": "[[SOUTH->Abandoned Car]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "North Field",
          "original": "[[NORTH->North Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "Scurring from your abandoned car on the bleak, shadowed interstate road, you make for the closest corn field to aid in your escape. You hear faint snarling in the distance."
    },
    {
     "name": "West Field",
      "tags": "",
      "id": "2",
      "text": "The West part of the field. The growling is still behind you, but is slightly fainter.\n\n[[WEST->Interstate]]\n[[NORTH->Scarecrow]]\n[[EAST-> Open Field]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "Interstate",
          "original": "[[WEST->Interstate]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "Scarecrow",
          "original": "[[NORTH->Scarecrow]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Open Field",
          "original": "[[EAST->Open Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "The West part of the field. The growling is still behind you, but is slightly fainter."
    },
    {
      "name": "East Field",
      "tags": "",
      "id": "3",
      "text": "The Eastmost section of the field. The growling has gotten louder in your right ear, which makes you panic.\n\n\n[[NORTH->Outhouse]]\n[[WEST->Northmost Field]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Outhouse",
          "original": "[[NORTH->Outhouse]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Northmost Field",
          "original": "[[WEST->Northmost Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Eastmost section of the field. The growling has gotten louder in your right ear, which makes you panic."
    },
    {
      "name": "Abandoned Car",
      "tags": "",
      "id": "4",
      "text": "You return to what you attempted to flee moments ago. Still panting, you slowly pace around the perimeter until you reach the trunk, which seems to pulsate in your shaky vision. Placing one hand on the hood, it feels almost hot to the touch.\n\nHow did it come to this? \n\nThe snarling has turned into human-like growling, rumbling in your chest. You crumple to the ground in anguish and defeat just as you feel the weight of a searingly hot hand touch the top of your head.\n\n\nTRY AGAIN\n\n[[FORWARD->Open Field]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Open Field",
          "original": "[[FORWARD->Open Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "You return to what you attempted to flee moments ago. Still panting, you slowly pace around the perimeter until you reach the trunk, which seems to pulsate in your shaky vision. Placing one hand on the hood, it feels almost hot to the touch.\n\nHow did it come to this? \n\nThe snarling has turned into human-like growling, rumbling in your chest. You crumple to the ground in anguish and defeat just as you feel the weight of a searingly hot hand touch the top of your head.\n\n\nTRY AGAIN"
    },
    {
      "name": "North Field",
      "tags": "",
      "id": "5",
      "text": "Heading straight for the center of the field, you make a beeline for any signs of the woman you seek- the only one who could possibly understand you. The growling can be heard directly behind you.\n\n[[NORTH->Northmost Field]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Northmost Field",
          "original": "[[NORTH->Northmost Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "Heading straight for the center of the field, you make a beeline for any signs of the woman you seek- the only one who could possibly understand you. The growling can be heard directly behind you."
    },
    {
      "name": "Interstate",
      "tags": "",
      "id": "6",
      "text": "Your feet hit pavement, your chest heaving. Stopping to turn, you witness the headlights of your abandoned car illuminating the road a good distance in front of you, but the distance between you and the car is tinged with red.\n\nYou feel sickened.\n\nMemories of a foul stench floods your memory and into your conscious, prompting you to lower and shake your head to help clear it. The malicious prescence feels closer than when you entered the field. Too close, even. \n\n\nTRY AGAIN\n\n[[FORWARD->Open Field]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Open Field",
          "original": "[[FORWARD->Open Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "Your feet hit pavement, your chest heaving. Stopping to turn, you witness the headlights of your abandoned car illuminating the road a good distance in front of you, but the distance between you and the car is tinged with red.\n\nYou feel sickened.\n\nMemories of a foul stench floods your memory and into your conscious, prompting you to lower and shake your head to help clear it. The malicious prescence feels closer than when you entered the field. Too close, even. \n\n\nTRY AGAIN"
    },
    {
      "name": "Scarecrow",
      "tags": "",
      "id": "7",
      "text": "After running a fair distance in the field, the sight of a humanoid figure prompts you to stumble slightly in fright. Slowly approaching, you realize that it is a denim overall-donned scarecrow, quietly mocking you for your misplaced panic. Amidst all that's happened, his stoic presence is almost welcoming.\n\nThe growling has gone silent.\n\n[[NORTH->Fence]]\n[[EAST->Dirt Path]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Fence",
          "original": "[[NORTH->Fence]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Dirt Path",
          "original": "[[EAST->Dirt Path]]"
        }
      ],
      "hooks": [],
      "cleanText": "After running a fair distance in the field, the sight of a humanoid figure prompts you to stumble slightly in fright. Slowly approaching, you realize that it is a denim overall-donned scarecrow, quietly mocking you for your misplaced panic. Amidst all that's happened, his stoic presence is almost welcoming.\n\nThe growling has gone silent."
    },
    {
      "name": "Open Field",
      "tags": "",
      "id": "8",
      "text": "Moving towards a break in the fields, you stop to catch your breath. Looking around, the area appears to have been shaved in a deliberate circle about 5 meters across. There are still no signs of life or of death.\n\n[[WEST->Northmost Field]] \n[[NORTH->Dirt Path]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "Northmost Field",
          "original": "[[WEST->Northmost Field]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "Dirt Path",
          "original": "[[NORTH->Dirt Path]]"
        }
      ],
      "hooks": [],
      "cleanText": "Moving towards a break in the fields, you stop to catch your breath. Looking around, the area appears to have been shaved in a deliberate circle about 5 meters across. There are still no signs of life or of death."
    },
    {
      "name": "Fence",
      "tags": "",
      "id": "9",
      "text": "You come to a shoddy, natural wood fence that comes to your waist. Unsure of what it's even here for, you attempt to jump the sad excuse of a fence when you feel your shin come in contact with the topmost stick.\n\nFalling headfirst into the soil underneath you, your head bounces off the ground slightly as your legs, victims of exhuastion and stress themselves, hit different parts of that same fence and force your body sideways. Lying in agony with tears forming from frustration, a controlled, steady sound of footsteps approaches from your left.\n\nAshamedly, you cannot even muster the strength to look up as they stop right by your left ear. They slightly shift as the figure raises its dark boot, sharply and forcefully bringing it down with as much otherworldly force as it can muster.\n\n\nTRY AGAIN\n\n[[FORWARD->Open Field]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Open Field",
          "original": "[[FORWARD->Open Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "You come to a shoddy, natural wood fence that comes to your waist. Unsure of what it's even here for, you attempt to jump the sad excuse of a fence when you feel your shin come in contact with the topmost stick.\n\nFalling headfirst into the soil underneath you, your head bounces off the ground slightly as your legs, victims of exhuastion and stress themselves, hit different parts of that same fence and force your body sideways. Lying in agony with tears forming from frustration, a controlled, steady sound of footsteps approaches from your left.\n\nAshamedly, you cannot even muster the strength to look up as they stop right by your left ear. They slightly shift as the figure raises its dark boot, sharply and forcefully bringing it down with as much otherworldly force as it can muster.\n\n\nTRY AGAIN"
    },
    {
      "name": "Dirt Path",
      "tags": "",
      "id": "10",
      "text": "Continuing on, you soon come to a long dirt path at a break between fields. Desperate for cover, you wonder if there are any places you can take cover in nearby. There has to be... there must be, you think in desperation.\n\n[[NORTH-> Widened Dirt Path]]\n[[EAST->Freshly-Dug Hole]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Widened Dirt Path",
          "original": "[[NORTH->Widened Dirt Path]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Freshly-Dug Hole",
          "original": "[[EAST->Freshly-Dug Hole]]"
        }
      ],
      "hooks": [],
      "cleanText": "Continuing on, you soon come to a long dirt path at a break between fields. Desperate for cover, you wonder if there are any places you can take cover in nearby. There has to be... there must be, you think in desperation."
    },
    {
      "name": "Widened Dirt Path",
      "tags": "",
      "id": "11",
      "text": "After running for a while, you finally come to what seems to be a building comprable to a shelter. You almost let out a squeak of joy, but you swallow it down, fearful of the consequences.\n\n[[EAST->Decrepit Shack]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "Decrepit Shack",
          "original": "[[EAST->Decrepit Shack]]"
        }
      ],
      "hooks": [],
      "cleanText": "After running for a while, you finally come to what seems to be a building comprable to a shelter. You almost let out a squeak of joy, but you swallow it down, fearful of the consequences."
    },
    {
      "name": "Freshly-Dug Hole",
      "tags": "",
      "id": "12",
      "text": "Deciding to slightly circumvent the road, you soon come upon a shallow, misshapen hole no longer than two meters across. A worn, slightly-rusted shovel pierces the soft earth not too far away. Whoever made this hole must've been in a significant rush.\n\nYou feel a wave of confidence and relief wash over you at this sign of life, prompting you to run faster.\n\n[[NORTH->Decrepit Shack]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Decrepit Shack",
          "original": "[[NORTH->Decrepit Shack]]"
        }
      ],
      "hooks": [],
      "cleanText": "Deciding to slightly circumvent the road, you soon come upon a shallow, misshapen hole no longer than two meters across. A worn, slightly-rusted shovel pierces the soft earth not too far away. Whoever made this hole must've been in a significant rush.\n\nYou feel a wave of confidence and relief wash over you at this sign of life, prompting you to run faster."
    },
    {
      "name": "Decrepit Shack",
      "tags": "",
      "id": "13",
      "text": "Finally close enough to the small building that you can get as good a look at it as you're able in the pitch darkness, you can see that there are extremely few traces of recent activity- the paint is chipped and the hardware is rusted. Your spirits drop slightly, but you press on.\n\n[[NORTH->Shack Interior]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Shack Interior",
          "original": "[[NORTH->Shack Interior]]"
        }
      ],
      "hooks": [],
      "cleanText": "Finally close enough to the small building that you can get as good a look at it as you're able in the pitch darkness, you can see that there are extremely few traces of recent activity- the paint is chipped and the hardware is rusted. Your spirits drop slightly, but you press on."
    },
    {
      "name": "Shack Interior",
      "tags": "",
      "id": "14",
      "text": "Once you wrestle open the surprisingly hefty door, the scent of freshly snuffed candles overwhelms your senses. Shutting the door with your back, you try and make out any figures as the last sliver of light is extinguished from the crack in the door. As your eyes adjust, you feel someone or something in the room.\n\n[[NORTH->Precisely Dug Hole]]\n[[SOUTH->Shack Exterior]]\n[[WEST->Altar]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Precisely Dug Hole",
          "original": "[[NORTH->Precisely Dug Hole]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Shack Exterior",
          "original": "[[SOUTH->Shack Exterior]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Altar",
          "original": "[[WEST->Altar]]"
        }
      ],
      "hooks": [],
      "cleanText": "Once you wrestle open the surprisingly hefty door, the scent of freshly snuffed candles overwhelms your senses. Shutting the door with your back, you try and make out any figures as the last sliver of light is extinguished from the crack in the door. As your eyes adjust, you feel someone or something in the room."
    },
    {
      "name": "Northmost Field",
      "tags": "",
      "id": "15",
      "text": "With no signs of anything or anyone in sight, you begin to feel dread in the pit of your stomach. Your mind races as your breaths become even more ragged.\n\nDid she trick me? Was it all a lie? Did I do all that... for nothing?\n\nTears start to form at the edges of your eyes, threatening to bead and spill.\n\nYou slow slightly once you spot a clearing amongst the crops.\n\n[[NORTH->Empty, Bare Doorframe]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Empty, Bare Doorframe",
          "original": "[[NORTH->Empty, Bare Doorframe]]"
        }
      ],
      "hooks": [],
      "cleanText": "With no signs of anything or anyone in sight, you begin to feel dread in the pit of your stomach. Your mind races as your breaths become even more ragged.\n\nDid she trick me? Was it all a lie? Did I do all that... for nothing?\n\nTears start to form at the edges of your eyes, threatening to bead and spill.\n\nYou slow slightly once you spot a clearing amongst the crops."
    },
    {
      "name": "Empty, Bare Doorframe",
      "tags": "",
      "id": "16",
      "text": "An unattached, solitary doorframe greets you in the center of the clearing.\n\nSlowing to a halt, your confusion leads to frustration. You were told differently- she is said to welcome those that need her. If this couldn't be classified as your time of need, what could?\n\nThe hair on the back of your neck rises, signaling that you're still being hunted. Frantically searching for any sort of options you have as you slightly tremble, you perk up once you recall mutterings of the word \"door\".\n\nAs a harsh wind sporadically rushes in your direction, your feet move before you have any real time to make a decision. They're near.\n\nAs you cross the threshold of the frame with long strides, your shut eyes close, almost painfully. Standing taut with your hands balled by your sides in front of the frame, one lid wrenches in silent prayer as you're greeted with the same scene as before you closed your eyes. \n\nBefore you can react, a single dark palm comes into your line of sight.\n\n\nTRY AGAIN\n\n[[FORWARD->Open Field]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Open Field",
          "original": "[[FORWARD->Open Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "An unattached, solitary doorframe greets you in the center of the clearing.\n\nSlowing to a halt, your confusion leads to frustration. You were told differently- she is said to welcome those that need her. If this couldn't be classified as your time of need, what could?\n\nThe hair on the back of your neck rises, signaling that you're still being hunted. Frantically searching for any sort of options you have as you slightly tremble, you perk up once you recall mutterings of the word \"door\".\n\nAs a harsh wind sporadically rushes in your direction, your feet move before you have any real time to make a decision. They're near.\n\nAs you cross the threshold of the frame with long strides, your shut eyes close, almost painfully. Standing taut with your hands balled by your sides in front of the frame, one lid wrenches in silent prayer as you're greeted with the same scene as before you closed your eyes. \n\nBefore you can react, a single dark palm comes into your line of sight.\n\n\nTRY AGAIN"
    },
    {
      "name": "Outhouse",
      "tags": "",
      "id": "17",
      "text": "The sight of anything other than crops has you excited, until you realize it's only a solitary outhouse. However, the sight of the outhouse door laying haphazardly on the ground next to it sparks concern deep from within.\n\nPeering inside as you slow down to look for clues, you see that it looks unused, yet is still crumbling. The hinges look like they've been frantically ripped from the frame, as if they were searching for something.\n\nThe growling has not changed. You feel distressed.\n\n[[WEST->Empty, Bare Doorframe]]\n[[NORTH->Fence]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "Empty, Bare Doorframe",
          "original": "[[WEST->Empty, Bare Doorframe]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "Fence",
          "original": "[[NORTH->Fence]]"
        }
      ],
      "hooks": [],
      "cleanText": "The sight of anything other than crops has you excited, until you realize it's only a solitary outhouse. However, the sight of the outhouse door laying haphazardly on the ground next to it sparks concern deep from within.\n\nPeering inside as you slow down to look for clues, you see that it looks unused, yet is still crumbling. The hinges look like they've been frantically ripped from the frame, as if they were searching for something.\n\nThe growling has not changed. You feel distressed."
    },
    {
      "name": "Precisely Dug Hole",
      "tags": "",
      "id": "18",
      "text": "As you move to the center of the room, you reach a methodically excavated hole in the shack's dirt floor. Vaguely familiar, your heart rate accelerates as you hope you've finally reached what you've been searching so desperately for.\n\nThe soil around the hole appears to have been patted down with a flat instrument, a rusty variety of which are littered around the perimeter.\n\nThe presence seems closer, but you are not afraid. You are comforted.\n\n[[NORTH->Woman]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Woman",
          "original": "[[NORTH->Woman]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you move to the center of the room, you reach a methodically excavated hole in the shack's dirt floor. Vaguely familiar, your heart rate accelerates as you hope you've finally reached what you've been searching so desperately for.\n\nThe soil around the hole appears to have been patted down with a flat instrument, a rusty variety of which are littered around the perimeter.\n\nThe presence seems closer, but you are not afraid. You are comforted."
    },
    {
      "name": "Shack Exterior",
      "tags": "",
      "id": "19",
      "text": "Feeling uneasy, you wrench the door to the shack back open to reveal the moonlit field once more. Apparently forgetting you are actively being pursued, you stop to wonder where she might be as you shut the door back behind you. The moonlight is blotted out just above your head, and you open your mouth wide in a silent scream of terror.\n\n\nTRY AGAIN\n\n[[FORWARD->Open Field]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Open Field",
          "original": "[[FORWARD->Open Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "Feeling uneasy, you wrench the door to the shack back open to reveal the moonlit field once more. Apparently forgetting you are actively being pursued, you stop to wonder where she might be as you shut the door back behind you. The moonlight is blotted out just above your head, and you open your mouth wide in a silent scream of terror.\n\n\nTRY AGAIN"
    },
    {
      "name": "Altar",
      "tags": "",
      "id": "20",
      "text": "Moving straight to the perimeter of the shack you were unable to make out within the darkness, you stumble upon a well-worn wooden altar prominent among the features of the wall.\n\nUpon it you find what appears to be a hand-carved idol that sparks excitement when the form sparks a deep recognition. She must be near. The littered pillar candles of various heights and shades of white and tan is little more than breathtaking to you- the grace of Her inspires warmth from within.\n\nSensing movement, you turn to face the presence that has been near since you entered.\n\n[[NORTH->Woman]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Woman",
          "original": "[[NORTH->Woman]]"
        }
      ],
      "hooks": [],
      "cleanText": "Moving straight to the perimeter of the shack you were unable to make out within the darkness, you stumble upon a well-worn wooden altar prominent among the features of the wall.\n\nUpon it you find what appears to be a hand-carved idol that sparks excitement when the form sparks a deep recognition. She must be near. The littered pillar candles of various heights and shades of white and tan is little more than breathtaking to you- the grace of Her inspires warmth from within.\n\nSensing movement, you turn to face the presence that has been near since you entered."
    },
    {
      "name": "Woman",
      "tags": "",
      "id": "21",
      "text": "She reveals herself when she senses your need for her. Emerging from the shadows and dust of the musty shack, she comes out brandishing a gentle yet telling smile- you've finally made it.\n\nYou rush forward, hands almost in a frozen begging position stretched in front of you. In response, her arms open to accept you.\n\nAs you gaze at her face in wonder, you stop frantically moving to her once you recognize her eyes as being frigidly devoid of emotion. If anything, they read almost disdainful. \n\nNot wanting to be in her bad graces, you hurriedly attempt to explain who you are, where you came from, and what you've done to warrant her generosity. With a simple wave of her hand, you're silenced.\n\nShe already knows. About your betrayal. About your pain. About your... resentment.\n\nAbout the cadaver in your trunk.\n\nAs she kneels by the hole, she looks up at you expectantly.\n\nIt's almost over.\n\nIn a series of quick motions, you lower yourself smoothly yet with deliberation, hands slightly shaking with a mix of apprehension and excitement. As you settle in, she moves closer- one grimy yet delicate hand moving to cover your eyes. This is the first step, and yet the most difficult. Few have found her, for she only appears to those who truly need her- the price is especially steep.\n\nAs her lips part to form divine words, your vision goes completely dark under the cover of her cold palm.\n\nYou've made it. You're home.\n\n[[FORWARD->Open Field]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Open Field",
          "original": "[[FORWARD->Open Field]]"
        }
      ],
      "hooks": [],
      "cleanText": "She reveals herself when she senses your need for her. Emerging from the shadows and dust of the musty shack, she comes out brandishing a gentle yet telling smile- you've finally made it.\n\nYou rush forward, hands almost in a frozen begging position stretched in front of you. In response, her arms open to accept you.\n\nAs you gaze at her face in wonder, you stop frantically moving to her once you recognize her eyes as being frigidly devoid of emotion. If anything, they read almost disdainful. \n\nNot wanting to be in her bad graces, you hurriedly attempt to explain who you are, where you came from, and what you've done to warrant her generosity. With a simple wave of her hand, you're silenced.\n\nShe already knows. About your betrayal. About your pain. About your... resentment.\n\nAbout the cadaver in your trunk.\n\nAs she kneels by the hole, she looks up at you expectantly.\n\nIt's almost over.\n\nIn a series of quick motions, you lower yourself smoothly yet with deliberation, hands slightly shaking with a mix of apprehension and excitement. As you settle in, she moves closer- one grimy yet delicate hand moving to cover your eyes. This is the first step, and yet the most difficult. Few have found her, for she only appears to those who truly need her- the price is especially steep.\n\nAs her lips part to form divine words, your vision goes completely dark under the cover of her cold palm.\n\nYou've made it. You're home."
    }
  ]
}

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

#

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Total moves: " + str(moves) + ", Score: " + str(score))
		print("You are located at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")


def get_input():
	response = input("Where would you like to go? ")
	response = response.upper().strip()
	return response


def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"].upper() == response:
				return link["passageName"]
	print("Please try again.")
	return location_label
#

location_label = "Open Field"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves =+ 1
	if "score" in current_location:
		score = score + current_location["score"]
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	render(current_location, score, moves)
	response = get_input()

print("End")
