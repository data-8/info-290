test = {
  'name': 'Question 2_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> -1 <= slope_from_minimize <= 0
          True
          >>> 0 <= intercept_from_minimize <= 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(slope_from_minimize, -0.6498374231570391)
          True
          >>> np.isclose(slope_from_minimize, 1.1988619620992735)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
