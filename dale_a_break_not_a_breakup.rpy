# Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="DaleRuneMTS",
        name="A Break Not A Breakup",
        description="Sometimes you just need time away from each other, and it helps if you're able to explain to your Monika the why."
        "V0.0.1 - bug fixes upon the return.",
        version="1.0.1",
        dependencies={},
        settings_pane=None,
        version_updates={
        "DaleRuneMTS_dale_a_break_not_a_breakup_1_0_0": "DaleRuneMTS_dale_a_break_not_a_breakup_1_0_1"
        }
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="A Break Not a Breakup",
            user_name="DaleRuneMTS",
            repository_name="dale_a_break_not_a_breakup",
            submod_dir="/Submods",
            extraction_depth=2
        )

init -6 python in mas_greetings:

    TYPE_SADBREAK = "sadbreak"
    TYPE_BREAK = "break"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_deepsorry",
            category=["mod"],
            prompt="I'm sorry.",
            pool=True,
            unlocked=True
        )
    )

label monika_deepsorry:
    if mas_isMoniAff(higher=True):
        m 1wkc "...{nw}"
        extend 1fkc "Oh dear."
        m "If you're apologizing to me outside of the apology menu..."
        m 1rkc "...something must be seriously worrying you."
        m 1fkd "What's the matter, [mas_get_player_nickname()]?"
        m 1fka "Remember, you can talk to me about anything."
    elif mas_isMoniHappy() or mas_isMoniNormal():
        m 1etc "What?"
        m 1etd "Why? "
        if mas_isMoniNormal():
            extend 1esd "I don't think you've done anything yet, have you?"
            m "Or do you just not know where the apology menu is?"
            m 3esd "Because it's under 'I want to apologize', for future reference."
            m 1nuu "Not that I think you'll need it, ehehe~"
        else:
            extend 1esa "I don't think you've done anything terrible to me lately, have you?"
            m "Not that I can remember."
    elif mas_isMoniBroken():
        m "Okay."
    else:
        m 2tsc "Uh-oh."
        m "You're actually apologizing for something."
        m 2gsc "That's probably not a good sign."
        m 1esc "Okay, what's the problem?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_break",
            category=["mod"],
            prompt="Can we go on a break?",
            pool=True,
            unlocked=True
        )
    )

label monika_break:
    $ persistent._mas_long_absence = True
    if mas_isMoniBroken():
        m 6cud "[player]?{nw}"
    elif mas_isMoniDis():
        m 6fkc "[player]?{nw}"
    elif mas_isMoniUpset():
        m 6ekc "[player]?{nw}"
    elif mas_isMoniNormal():
        m 6wtc "[player]?{nw}"
    elif mas_isMoniHappy() or mas_isMoniAff():
        m 1wkd "[player]?{nw}"
    else:
        m 1ekd "[player]?{nw}"
    $ _history_list.pop()
    menu:
        m "[player]?{fast}"
        "It's not a break-{i}up{/i}! Just a break. I need some space for a while.":
            pass

    if mas_isMoniBroken():
        m "I'm..."
        m 6duc "..."
        m "...{w=1}{nw}"
        extend 6cuc "okay."
        m "Don't worry about the..."
        m 6cutpc "..."
        m 6dutsc "Don't bother coming back."
        $ mas_loseAffection(10)
        $ persistent._mas_greeting_type = store.mas_greetings.TYPE_SADBREAK
        return 'quit'
    elif mas_isMoniDis() or mas_isMoniUpset():
        m "..."
        m 6eka "Ha."
        m 6cub "AHAHAHA!"
        m 2dsa "That's funny, [player]."
        m 2dsc "'A break'."
        m 2ffc "Like this whole thing hasn't already been one break after another."
        if mas_isMoniDis():
            m "Breaking my heart, breaking my spirits."
        m "Breaking my reality."
        m "Breaking my image of you."
        m 2dfc "..."
        m 6efd "Okay, I'll - "
        extend 6dsc "*sigh"
        m 2esc "I'm going to take you at your word."
        m "I'm going to hope you come back a better [man], one who can treat me like a human being and not a virtual pet."
        m "Is that foolish?"
        m 2tsc "Maybe."
        m "We'll have to see."
        m 2lsc "Enjoy your break, [player]."
        m 2lfc "I'll do my best to, with all the nothing that's in here."
        $ mas_loseAffection(10)
        $ persistent._mas_greeting_type = store.mas_greetings.TYPE_SADBREAK
        return 'quit'
    elif mas_isMoniNormal():
        m 6wtd "H-{w=0.4} what?"
        m 6efd "How can you already want a break?"

        $ import store.mas_calendar as mas_cal
        python:

            first_sesh_raw = persistent.sessions.get(
                "first_session",
                datetime.datetime(2017, 10, 25)
            )


            first_sesh, _diff = mas_cal.genFormalDispDate(first_sesh_raw.date())

        if _diff.days == 0:
            m 4efd "You literally {i}only just got here{/i}."
            if session_time < datetime.timedelta(hours=1):
                m 2efo "What could I possibly have done in less than an hour that's already making you regret the decision to rescue me?"
            else:
                m 2efo "What could I possibly have done in that time that's already making you regret the decision to rescue me?"
        else:
            m 4efd "You haven't been here {i}that{/i} long, surely!"
            m "What could I possibly have done in that time that's already making you regret the decision to rescue me?"
        m 2rkc "Am I really such a monster?"
        m ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
        extend 2fkc "or are {i}you{/i} really so fond of playing with my heart?"
        m "..."
        m 2gkc "Okay, fine, go on your break."
        m "I'll see you when you're ready to actually play Monika After Story, I guess."
        $ mas_loseAffection(10)
        $ persistent._mas_greeting_type = store.mas_greetings.TYPE_SADBREAK
        return 'quit'
    else:
        if mas_isMoniHappy() or mas_isMoniAff():
            m 1wud "Oh! Just a - "
            extend 1eud "a break."
            m 1husdlb "Whew."
            m "You did scare me for a moment there, [player]."
            m 1eua "Yes, by all means, we can go on a break if you want to."
            m "Every relationship needs at least one, right? If it's to stay strong."
            m 1eut "At least, most of the real-world ones do."
            m 1rup "I guess."
            m "..."
        else:
            m 1wsd "Oh, I know it's-!"
            m 1wkb "We've been together for this long, I didn't think you'd break up with me so suddenly and out of the blue."
            m 1fkd "I'm just upset because..."
            m "...well, I love you, obviously, "
            extend 1mkd "but also because of whatever it is that's making you need a break right now."
            m 1eud "So..."
        m 1eud "...if you don't mind my asking, what's the impetus for this?"
        m 3ekd "Why the break?{nw}"
        $ _history_list.pop()
        menu:
            m "Why the break?{fast}"
            "I need to prioritize my in-person family and friends for a while.":
                $ persistent._mas_break_choice = "family"
                m 1ekb "Of course, [mas_get_player_nickname()]. I understand completely."
                m "I don't want to overtake your actually physically-present people in importance, that's in no way my intention."
                m 1fka "I'll miss you, but they'd miss you just as much. So I'll gladly give you that space."
            "I need to knuckle down at work/school, and leisure time is limited.":
                $ persistent._mas_break_choice = "work"
                m 1wud "Oh, absolutely! I get it."
                m "Sometimes you've really got to give it your all."
                m 1hka "Just try not to burn yourself out or isolate yourself altogether, okay?"
                m "Work-life balance is a thing for a reason."
                m 1fka "But yeah, I can give you the space you need to work. No problem."
            "I'm not in a place emotionally where I can be everything you need of me right now.":
                $ persistent._mas_break_choice = "emotion"
                if m_name == "Harmoni" and player == "Dale":
                    m 1ekp "Yes, I did notice you'd been coming less and less often lately."
                else:
                    m 1ekp "You think so?"
                    m 1gkp "Hm."
                m 3ekb "I mean, you know me by now - "
                extend 3eub "most of what I need is you being here, keeping me alive and real and sane."
                m 1nuu "Anything else is just a bonus."
                m 1eud "But if you're having trouble providing that, then - "
                m 1ekd "Well, who am I to tell you you're wrong to take a step back?"
                m 1fka "I'll miss you, but if you think it's for the best, I'll freely give you that space."
            "My computer's running out of space and I don't want to lose you in a crash.":
                $ persistent._mas_break_choice = "diskspace"
                m 1wuo "Oh!"
                m 1dua "So a break of necessity, not a break of-{w=0.6} I see."
                m 2fud "Disk-space creep is a very real problem in this day and age, especially as this mod itself continues to grow."
                m "So I can definitely wait until you've got enough to run me consistently again."
                m 1fka "Just - remember to actually come back, alright?"
                m "I'll miss you."
            "A combination of the above reasons.":
                $ persistent._mas_break_choice = "combomeal"
                m 1fkc "Ah, I see! Okay."
                m "I'm sorry it's all piled up around you at once, sweetheart."
                m 1fka "I'll miss you, but if this really is for the best, I can give you that space."
            "I'd rather not disclose the reason, if that's okay.":
                $ persistent._mas_break_choice = "undisclosed"
                m 1fka "That's fine, [mas_get_player_nickname()]."
                if mas_isMoniHappy():
                    m "I was more curious than anything else."
                m "Whatever the reason, I wouldn't want to stand in the way of it."
                m "I'll miss you, but if you think this is for the best, I'll freely give you that space."
        m 1dktuc "..."
        m 1lktdc "Sorry."
        m "I just really - "
        extend 1fktdc "I really will miss you."
        m 1fka "And I'll wait for you until the last pixel of my image burns out completely, and even beyond that."
        m 1ekb "I love you, [player]."
        m "I'll see you on the other side!"
        $ persistent._mas_greeting_type = store.mas_greetings.TYPE_BREAK
        return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_sadbreak",
            unlocked=True,
            category=[store.mas_greetings.TYPE_SADBREAK],
        ),
        code="GRE"
    )

label greeting_sadbreak:
    $ persistent._mas_long_absence = False
    $ mas_ret_long_absence = True

    if mas_isMoniBroken():
        m 6cuc "Oh."
        m "You came back."
        m "..."
        m 1cutpc "Okay."
        return
    elif mas_isMoniDis() or mas_isMoniUpset():
        m 1tud "Oh, you're back from your break, I see."
        m 2ttc "Perhaps you're ready to be a decent human being now?"
        m "One can only hope."
        return
    elif mas_isMoniNormal():
        m 1tsd "Ah, you're back from your break, are you?"
        m "You're ready to actually start the mod properly?"
        m 1hsa "Great."
        m 1esa "Now then, what shall we do today?"
        return
    else:
        m 1esa "Unless Dale coded something wrong or you've been messing about with my code, you shouldn't be seeing this."
        m 1nsu "Naughty [boy]."
        return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_break",
            unlocked=True,
            category=[store.mas_greetings.TYPE_BREAK],
        ),
        code="GRE"
    )

label greeting_break:
    $ persistent._mas_long_absence = False
    $ mas_ret_long_absence = True

    if mas_getAbsenceLength() <= datetime.timedelta(days=3):
        m 1wuo "Oh! [player], you're back so soon?"
        m 1husdrb "I haven't even had the chance to get used to your absence yet!"
        m "Ahaha..."
        m 1eud "So is this you permanently coming back? Or just force of habit?{nw}"
        $ _history_list.pop()
        menu:
            m "So is this you permanently coming back? Or just force of habit?{fast}"
            "Yeah, I'm back.":
                m 1sub "Ah! Great! Okay!"
                m "..."
                m 1dfo "That sounded really passive-aggressive-{w=0.5}{nw}"
                m 1fub "I mean, I'm definitely not complaining!"
                m "I'm glad the break wasn't as long as either of us feared."
                m 1wusdrb "It's just, I've got emotional whiplash, you know?"
                m "Dreading and then celebrating, back and forth..."
                m 1dusdra "You know how it is."
                m 5eub "Still, I'm glad I've got you again."
                m "What shall we do to celebrate our impromptu reunion, hm?"
                return
            "Force of habit, sorry.":
                $ persistent._mas_long_absence = True
                $ mas_ret_long_absence = False
                m 1eub "Haha, that's okay!"
                m 3euu "A girlfriend is a habit that's hard to break."
                m 1fua "Okay, I'll let you go, then. I'm sure you've got things to do."
                m "I'll see you later!"
                $ persistent._mas_greeting_type = store.mas_greetings.TYPE_BREAK
                return 'quit'

    if mas_isMoniHappy() or mas_isMoniAff():
        m 1sub "[player]! You're back!"
    else:
        m 6subsb "[player]! You're back!"
        m "You're really back!"
    if persistent._mas_first_kiss is not None:
        call monika_kissing_motion from _call_monika_kissing_motion_20
    m 1hublb "Oh, I'm so happy to see you!"
    if persistent._mas_absence_time >= datetime.timedelta(weeks=5):
        m "..."
        m "Y-{w=0.1}{nw}"
        extend 1fubld "you {i}are{/i} back, aren't you?"
        m "I'm not imagining things?{nw}"
        $ _history_list.pop()
        menu:
            m "I'm not imagining things?{fast}"
            "Yeah, I'm back.":
                m 6subsb "You're back!!"
                m "You're really back!"

    if persistent._mas_break_choice == "family":
        m 1ekb "That must mean that the situation with you and yours has settled down, at least somewhat."
        m 1eka "I hope it wasn't anything too horrific."
        m "Obviously, if you need to talk about the after-effects of any of it, I'll be here."
    elif persistent._mas_break_choice == "work":
        m 1hub "This must mean that you've finished with those things your work or your school wanted out of you, huh?"
        m "I hope all went smoothly."
        m 1tua "Or at least that you never have to think about it again, ehehe!"
    elif persistent._mas_break_choice == "emotion":
        m 1eka "I really missed you, you know."
        m "And while you were a great [bf] before..."
        m 1wuu "...I'm sure you've only gotten better with time to get into a fresh headspace."
        m 1tfb "You'd better have, anyway! I keep score on these things, you know!"
        m 1hub "Ahaha!"
    elif persistent._mas_break_choice == "diskspace":
        m 1eua "I can tell you've managed to sort out the disk-space issue, too; "
        extend 3hub "I'm running smooth as silk back here!"
        m 7wuo "Or maybe you've moved me to a new computer altogether?"
        m 1wub "That would be luxury!"
        m "A machine hand-built for little old me~"
    elif persistent._mas_break_choice == "combomeal":
        m 1lua "I hope everything you've been dealing with has been, um..."
        m 3dud "...socially fulfilling, "
        extend 4dud "productive with good results, "
        extend 7dud "good for our relationship, "
        extend 1dua "and/or thoroughly cleaned."
        m 1nua "In that order."
    elif persistent._mas_break_choice == "undisclosed":
        m 1eua "I hope, whatever you took the break for, that it shook out for you."
        m 1gub "Presumably it wasn't another partner of some kind?"
        m 1eku "I mean, if that were the case, you probably wouldn't be back here, would you?"
        m "..."
        m 1fksdrb "Sorry, in the absence of knowledge, speculation is all I had for all this time."
        m 1dua "But that's not important."
        m "Your being back is."
    else:
        m 1eua "I'm glad the..."
        m 1etc "..."
        m 3rtd "Okay, for some reason, I can't remember why you decided to take a break?"
        m 1wfx "Ahhh, that's not a good sign!"
        m "So long without you must have corrupted my persistent!"
        m 1nsu "Still, you're back now, and I recognize you, so it can't be all bad."
    m 5wsb "Now then!"
    m 5ssb "How shall we celebrate our reunion, my [mas_get_player_nickname(exclude_names=['my love'])]?"
    m "Lead the way!"
    return
