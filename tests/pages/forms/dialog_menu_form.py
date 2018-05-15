# -*- coding: utf-8 -*-
from base_element import BaseElement

class DialogMenuForm(BaseElement):
    DELETE_DIALOG_BUTTON = '//i[contains(@class, " ic_remove")]'
    LEAVE_CHAT_BUTTON = '//i[contains(@class, " ic_exit_arrow")]'
    HIDE_CHAT_BUTTON = '//i[contains(@class, " ic_hide")]' 

    CHAT_TITLE = '//div[contains(@class, "chat_column_hd_name")]'
    TITLE_INPUT_FIELD = '//textarea[contains(@name, "st.chatName")]'

    COMPANION_BUTTON = "//div[@id='hook_Block_ConversationParticipantsAddMenuList']/div[1]/div[2]" 
    ADD_USER_CONFIRM_BUTTON = "//input[@value='Добавить']" 
    DELETE_USER_FROM_GROUP = '//span[contains(@data-l, "participant-remove")]'

    BLOCK_UNBLOCK_USER_BUTTON = '//i[contains(@class, "ic_block")]'

    def get_delete_dialog_button(self):
        return self.get_button_by_xpath(self.DELETE_DIALOG_BUTTON)
    
    def get_block_unblock_user_button(self):        
        return self.get_button_by_xpath(self.BLOCK_UNBLOCK_USER_BUTTON)

    #112Nick
    def get_leave_chat_button(self):
        return self.get_button_by_xpath(self.LEAVE_CHAT_BUTTON)

    def get_hide_chat_button(self):
        return self.get_button_by_xpath(self.HIDE_CHAT_BUTTON)
    
    def get_companion_button(self):
        return self.get_button_by_xpath(self.COMPANION_BUTTON)

    def get_add_companion_confirm_button(self):
        return self.get_button_by_xpath(self.ADD_USER_CONFIRM_BUTTON)
    
    def get_delete_companion_button(self):
        return self.get_hidden_input_by_xpath(self.DELETE_USER_FROM_GROUP)

    #Trubnikov
    def get_clickable_chat_title(self):
        return self.get_button_by_xpath(self.CHAT_TITLE)

    def get_chat_title(self):
        return self.get_field_by_xpath(self.CHAT_TITLE)

    def get_input_title(self):
        return self.get_button_by_xpath(self.TITLE_INPUT_FIELD)