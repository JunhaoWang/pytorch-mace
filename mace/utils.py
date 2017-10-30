def debug(fn):
	def tracer(*args):
		strs = (str(arg) for arg in args)
		print('{}({})'.format(fn.__name__,', '.join(strs)))
		try:
			return fn(*args)
		except:
			# import pdb
			# pdb.set_trace()
			print('error occured at {}'.format(fn.__name__))
			return None
	return tracer