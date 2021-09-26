import warnings

class metaMetaBunch(type):
  # metaclass for new and improved "Bunch": implicitly defines \texttt{__}\emph{slots}\texttt{__}, \texttt{__}\emph{init}\texttt{__} and \texttt{__}\emph{repr}\texttt{__} 
  # from variables bound in class scope. An instance of \emph{metaMetaBunch} (a class whose metaclass 
  # is \emph{metaMetaBunch}) defines only class-scope variables (and possibly special methods, but
  # NOT \texttt{__}\emph{init}\texttt{__} and \texttt{__}\emph{repr}\texttt{__}!).  \emph{metaMetaBunch} removes those variables from class scope,  
  # snuggles them instead as items in a class-scope dict named \texttt{__}\emph{dflts}\texttt{__}, and puts in the class a
  #  \texttt{__}\emph{slots}\texttt{__} listing those variables' names, an \texttt{__}\emph{init}\texttt{__} that takes as optional keyword 
  # arguments each of them (using the values in \texttt{__}\emph{dflts}\texttt{__} as defaults for missing ones), and
  # a \texttt{__}\emph{repr}\texttt{__} that shows the repr of each attribute that differs from its default value (the output
  # of \texttt{__}\emph{repr}\texttt{__} can be passed to \texttt{__}\emph{eval}\texttt{__} to make an equal instance, as per the usual convention 
  # in the matter).

  def __new__(cls, classname, bases, classdict):
    # Everything needs to be done in \texttt{__}\emph{new}\texttt{__}, since type.\texttt{__}\emph{new}\texttt{__} is where \texttt{__}\emph{slots}\texttt{__} are taken
    # into account.

    # Define as local functions the \texttt{__}\emph{init}\texttt{__} and \texttt{__}\emph{repr}\texttt{__} that we'll use in the new class.

    def __init__(self, **kw):
      # Simplistic \texttt{__}\emph{init}\texttt{__}: first set all attributes to default values, then override those explicitly 
      # passed in \emph{kw}.

      for k in self.__dflts__: setattr(self, k, self.__dflts__[k])
      for k in kw: setattr(self, k, kw[k])

    def __repr__(self):
      # Clever \texttt{__}\emph{repr}\texttt{__}: show only attributes that differ from the respective default values,
      # for compactness.

      rep = [ '%s=%r' % (k, getattr(self, k)) for k in self.__dflts__
              if getattr(self, k) != self.__dflts__[k]]
      return '%s(%s)' % (classname, ', '.join(rep))

      # Build the newdict that we'll use as class-dict for the new class
      newdict = {'__slots__':[], '__dflts__':{}, '__init__':__init__, '__repr__':__repr__}

    for k in classdict:
      if k.startswith('__'):
        # Special methods: copy to \emph{newdict}, warn about conflicts.
        if k in newdict:
          warnings.warn("Can't set attr %r in bunch-class %r" % (k, classname))
        else:
          newdict[k] = classdict[k]
      else:
        # Class variables, store name in \texttt{__}\emph{slots}\texttt{__} and name and value as an item in \texttt{__}\emph{dflts}\texttt{__}.
        newdict['__slots__'].append(k)
        newdict['__dflts__'][k] = classdict[k]
    # Finally delegate the rest of the work to \emph{type}.\texttt{__}\emph{new}\texttt{__}
    return type.__new__(cls, classname, bases, newdict)

class record(object):
  # For convenience: inheriting from \emph{record} can be used to get the new metaclass (same as 
  # defining \texttt{__}\emph{metaclass}\texttt{__} yourself).
  __metaclass__ = metaMetaBunch


if __name__ == "__main__":
  # Example use: a \emph{record} class.
  class Point(record):
    # A point has $x$ and $y$ coordinates, defaulting to 0.0, and a color, defaulting to \texttt{'gray'} -- and 
    # nothing more, except what Python and the metaclass conspire to add, such as \texttt{__}\emph{init}\texttt{__} 
    # and \texttt{__}\emph{repr}\texttt{__}.
    x = 0.0
    y = 0.0
    color = 'gray'

  # Example uses of class \emph{Point}.
  q = Point()
  print q

  p = Point(x=1.2, y=3.4)
  print p

  r = Point(x=2.0, color='blue')
  print r
  print r.x, r.y
