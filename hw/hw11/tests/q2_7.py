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
          >>> np.round(slope_from_minimize, 4)
          -0.6498
          >>> np.round(intercept_from_minimize, 4)
          1.1989
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
