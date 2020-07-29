#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Autenticacion KB de QnATest Indra """
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    #7740c0ef-4e61-419a-a8af-aa6ab3647726
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    #wJlL|aDoXKq)OeXT]{6t{iWfOEvgw7y
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "ebc3edff-0672-45b0-a6fd-404b467bf19e")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "e75add48-dd03-427a-821b-129965bcc03a")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://s0testqnaindra.azurewebsites.net/qnamaker")
