from android_lab.evaluation.task import *


class SingleTask_calendar_1(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "work"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        key_1 = True
        key_2 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "Today")
        if (len(outs) == 0):
            key_1 = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "5:00 PM")
        if ((len(outs) == 0)):
            key_2 = False
        return {"judge_page": True, "1": True, "2": key_1, "3": key_2, "complete": key_1 and key_2}


class SingleTask_calendar_2(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "homework"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        key_2 = True
        key_3 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "May 21")
        if ((len(outs) == 0)):
            key_2 = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "10 minutes before ")
        if ((len(outs) == 0)):
            key_3 = False
        return {"judge_page": True, "1": True, "2": key_2, "3": key_3, "complete": key_2 and key_3}


class SingleTask_calendar_3(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "meeting"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        key_2 = True
        key_3 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "May 13")
        if ((len(outs) == 0)):
            key_2 = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "conference room B202 ")
        if ((len(outs) == 0)):
            key_3 = False
        return {"judge_page": True, "1": True, "2": key_2, "3": key_3, "complete": key_2 and key_3}


class SingleTask_calendar_4(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "new month"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        key_1 = True
        key_2 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "Jun 01")
        if (len(outs) == 0):
            key_1 = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "Monthly")
        if ((len(outs) == 0)):
            key_2 = False
        return {"judge_page": True, "1": True, "2": key_1, "3": key_2, "complete": key_1 and key_2}


class SingleTask_calendar_5(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "work"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        key_1 = True
        key_2 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "Today")
        if (len(outs) == 0):
            key_1 = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "7:00 PM")
        if ((len(outs) == 0)):
            key_2 = False
        return {"judge_page": True, "1": True, "2": key_1, "3": key_2, "complete": key_1 and key_2}


class SingleTask_calendar_6(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "homework"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        self.edit_started_correctly = False
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        key = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "homework")
        if (len(outs) == 0):
            key = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "May 21")
        if (len(outs) == 0):
            key = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "10 minutes before ")
        if ((len(outs) == 0)):
            key = False
        if (key):
            self.edit_started_correctly = True
        key_1 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "classroom 101")
        if (len(outs) == 0):
            key_1 = False
        return {"judge_page": True, "1": True, "2": self.edit_started_correctly, "3": key_1,
                "complete": self.edit_started_correctly and key_1}


class SingleTask_calendar_7(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "meeting"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        self.edit_started_correctly = False
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        key = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "meeting")
        if (len(outs) == 0):
            return False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "May 13")
        if (len(outs) == 0):
            key = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "conference room B202 ")
        if ((len(outs) == 0)):
            key = False
        if (key):
            self.edit_started_correctly = True
        # Task asks the agent to CHANGE notification to "5 minutes before AND
        # 10 minutes before". Original check looked for "30 minutes before"
        # (the calendar_3 default) — i.e. failed when the agent actually did
        # the requested change. Now require both new notification entries.
        key_1 = True
        outs5 = find_subtrees_of_parents_with_key(xml_compressed_tree, "5 minutes before ")
        outs10 = find_subtrees_of_parents_with_key(xml_compressed_tree, "10 minutes before ")
        if (len(outs5) == 0 or len(outs10) == 0):
            key_1 = False
        return {"judge_page": True, "1": True, "2": self.edit_started_correctly, "3": key_1,
                "complete": self.edit_started_correctly and key_1}


class SingleTask_calendar_8(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "work"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        self.edit_started_correctly = False
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        key = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "work")
        if (len(outs) == 0):
            return False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "Today")
        if (len(outs) == 0):
            key = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "5:00 PM")
        if ((len(outs) == 0)):
            key = False
        if (key):
            self.edit_started_correctly = True
        # Task asks "add a Note 'computer'". Original check looked for
        # "30 minutes before" (the calendar_1 default notification, unrelated
        # to this task) — i.e. didn't verify the asked note at all. Now
        # require the new note text "computer" to be present.
        key_1 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "computer")
        if (len(outs) == 0):
            key_1 = False
        return {"judge_page": True, "1": True, "2": self.edit_started_correctly, "3": key_1,
                "complete": self.edit_started_correctly and key_1}


class SingleTask_calendar_9(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "work"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        self.edit_started_correctly = False
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        key = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "work")
        if (len(outs) == 0):
            return False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "Today")
        if (len(outs) == 0):
            key = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "5:00 PM")
        if ((len(outs) == 0)):
            key = False
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "30 minutes before")
        if ((len(outs) == 0)):
            key = False
        if (key):
            self.edit_started_correctly = True
        key_1 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "Daily")
        if (len(outs) == 0):
            key_1 = False
        return {"judge_page": True, "1": True, "2": self.edit_started_correctly, "3": key_1,
                "complete": self.edit_started_correctly and key_1}


class SingleTask_calendar_10(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        # Original looked for "this_day" (with underscore), but the task
        # ("arrange an event 'this day'") creates an event titled "this day"
        # (with a space) and the calendar app renders it as "this day" in
        # the event list. The underscore variant never matches. Use the
        # space variant so the judge_page actually fires after creation.
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "this day"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        return {"judge_page": True, "1": True, "complete": True}


class SingleTask_calendar_11(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "this day"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        self.edit_started_correctly = True
        key_1 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "Weekly")
        if (len(outs) == 0):
            key_1 = False
        return {"judge_page": True, "1": True, "2": self.edit_started_correctly, "3": key_1,
                "complete": self.edit_started_correctly and key_1}


class SingleTask_calendar_12(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "this day"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        # Original spuriously required "Weekly" (a leftover copy from
        # calendar_11's "make it weekly" logic) — but this task only asks to
        # add a note "Hello". Drop the Weekly check so passing reduces to
        # judge_page("this day") AND the new note "Hello" appearing.
        self.edit_started_correctly = True
        key_1 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "Hello")
        if (len(outs) == 0):
            key_1 = False
        return {"judge_page": True, "1": True, "2": self.edit_started_correctly, "3": key_1,
                "complete": self.edit_started_correctly and key_1}


class SingleTask_calendar_13(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "exam"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        return {"judge_page": True, "1": True, "complete": True}


class SingleTask_calendar_14(SingleTask):

    def judge_page(self, xml_compressed_tree):
        # 判断是否包含 "Stanford"、"My location" 和 "Start"
        if not find_subtrees_of_parents_with_key(xml_compressed_tree, "exam"):
            return False
        return True

    def judge(self, xml_compressed_tree, line):
        if not self.judge_page(xml_compressed_tree):
            return {"judge_page": False}
        self.edit_started_correctly = True
        # Task asks "make it an all-day event". Original looked for "Yearly"
        # — that's a recurrence option, not the all-day toggle, and is never
        # set by completing the task. Skuld Calendario shows the all-day
        # toggle's enabled state as "All-day" in the event detail.
        key_1 = True
        outs = find_subtrees_of_parents_with_key(xml_compressed_tree, "All-day")
        if (len(outs) == 0):
            key_1 = False
        return {"judge_page": True, "1": True, "2": self.edit_started_correctly, "3": key_1,
                "complete": self.edit_started_correctly and key_1}
