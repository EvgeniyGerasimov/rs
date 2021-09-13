from locust import HttpUser, between, task
import random
import users
import items


class WebsiteUser(HttpUser):
    # wait_time = between(1, 1)
    host = "https://lab.motorsportnetwork.com/"

    def get_article(self):
        article_id = items.items
        return random.choice(article_id)

    def get_user(self):
        user_id = users.users
        return random.choice(user_id)

    @task(1)
    def client_visit(self):
        clientId = self.get_user()
        article_edition_id = self.get_article()
        body = {
            'clientId': clientId,
            'article_edition_id': article_edition_id
        }
        self.client.post("recommend", json=body)


    @task(2)
    def unknow_user_visiy(self):
        article_edition_id = self.get_article()
        self.client.post("recommend", json={
            'clientId': None,
            'article_edition_id': article_edition_id
        })
