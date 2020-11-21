test = {
  'name': 'Question 3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(fit_line(Table().with_columns('x', make_array(0, 1), 'y', make_array(1, 3)))) == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(fit_line(faithful).item(0), 10.7296414)
          True
          >>> np.isclose(fit_line(faithful).item(1), 33.47439702)
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
