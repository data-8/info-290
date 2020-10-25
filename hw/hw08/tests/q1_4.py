test = {
  'name': 'Question 1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> -1 <= diff_lower_bound <= diff_upper_bound <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.0 <= diff_lower_bound <= 0.07
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.1 <= diff_upper_bound <= 0.17
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
