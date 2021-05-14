import github


class Stargazer(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Stargazers. The reference can be found here https://docs.github.com/en/rest/reference/activity/starring#alternative-response-with-star-creation-timestamps
    """

    def __repr__(self):
        return self.get__repr__({"user": self._user.value._login.value})

    @property
    def starred_at(self):
        """
        :type: datetime.datetime
        """
        return self._starred_at.value

    @property
    def user(self):
        """
        :type: :class:`github.NamedUser`
        """
        return self._user.value

    def _initAttributes(self):
        self._starred_at = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "starred_at" in attributes:
            self._starred_at = self._makeDatetimeAttribute(attributes["starred_at"])
        if "user" in attributes:
            self._user = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["user"]
            )