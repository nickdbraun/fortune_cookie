#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getrandomfortune():
    fortunes =[
    "I see you will do well",
    "LaunchCode will do many things for you",
    "Much money in your future"
    ]

    index = random.randint(0,2)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getrandomfortune()+"</strong>"
        fortune_sent = "Your Fortune is:" + fortune
        fortune_para = "<p>"+fortune_sent+"</p>"

        lucky_number = "<strong>" +str(random.randint(1,100)) + "</strong>"
        number_sentence = "Your lucky number:" + str(lucky_number)
        number_para = "<p>"+number_sentence+"</p>"

        again = "<a href='.'><button>Another Fortune!</button></a>"

        content= header + number_para + fortune_para + again

        self.response.out.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
