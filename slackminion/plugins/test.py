from ..plugin import BasePlugin, cmd, webhook


class TestPlugin(BasePlugin):

    @cmd()
    def echo(self, msg, args):
        """Simply repeats whatever is said."""
        self.log.debug("Received args: %s", args)
        return ' '.join(args)

    @cmd()
    def xyzzy(self, msg, args):
        """Nothing happens."""
        return "Nothing happens for %s" % msg.user

    @cmd()
    def alert(self, msg, args):
        """Alert everyone."""
        self.send_message(self.config['channel'], '<!here>: something important is going to happen!')
        return None

    @webhook('/echo', form_params='foo')
    def web_echo(self, foo):
        self.send_message(self.config['channel'], foo)


class TestAclPlugin(BasePlugin):

    @cmd(admin_only=True)
    def admincmd(self, msg, args):
        """A command only admins should be able to run."""
        return ':boom:'

    @cmd(acl='test')
    def acltest(self, msg, args):
        """A command only members of 'acltest' should be able to run."""
        return ':sushi:'

    @cmd(admin_only=True, acl='test')
    def adminacl(self, msg, args):
        """Only admins who are in 'acltest' should be able to run this."""
        return ':godmode:'
