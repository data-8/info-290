test = {
  'name': 'Question 2_8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 10.9 <= best_total_squared_error <= 14
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(best_total_squared_error, 10.975003568216033)
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
