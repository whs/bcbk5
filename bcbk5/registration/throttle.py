from rest_framework.throttling import ScopedRateThrottle

class PostScopedRateThrottle(ScopedRateThrottle):
	def allow_request(self, request, view):
		# if we check for post
		# could be a vulnerability for other methods
		if request.method == 'GET':
			return True

		return super(PostScopedRateThrottle, self).allow_request(request, view)