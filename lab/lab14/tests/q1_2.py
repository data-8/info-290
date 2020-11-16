test = {
  'name': 'Question 1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> train_movements.num_rows == num_train
          True
          >>> test_movements.num_rows + num_train == num_movements
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> train_movements.num_rows
          660
          >>> test_movements.num_rows
          300
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
