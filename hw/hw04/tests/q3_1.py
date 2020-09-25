test = {
  'name': 'Question 3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> prof_names.num_columns
          2
          >>> prof_names.num_rows
          71
          >>> prof_names.labels[1]
          'faculty'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prof_names.column(0).item(0)
          'African American Studies'
          >>> type(prof_names.column(1).item(0))
          numpy.ndarray
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
