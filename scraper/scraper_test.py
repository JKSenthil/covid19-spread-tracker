import unittest

from extract import extract_counties_and_cases

# Sample data from 2020/03/22, NEW YORK
DATA = [
    'New York', '+1534', '9654', '+3', '63', '0.7%',
    'Nassau', '+666', '1900', '4', '0.2%',
    'Westchester', '+486', '1873', '0', '0%',
    'Suffolk', '+372', '1034', '+3', '12', '1.2%',
    'Rockland', '+193', '455', '1', '0.2%',
    'Orange', '+84', '247', '0', '0%',
    'Albany', '+35', '123', '0', '0%',
    'Dutchess', '+33', '82', '+1', '1', '1.2%',
    'Monroe', '+22', '68', '1', '1.5%',
    'Erie', '56', '0', '0%',
    'Onondaga', '+11', '45', '0', '0%',
    'Saratoga', '35', '0', '0%',
    'Schenectady', '32', '0', '0%',
    'Putnam', '31', '0', '0%',
    'Unassigned', '+23', '23', '+34', '34', '147.8%',
    'Rensselaer', '20', '0', '0%',
    'Ulster', '18', '0', '0%',
    'Columbia', '+10', '17', '0', '0%',
    'Tompkins', '+3', '15', '0', '0%',
    'Sullivan', '12', '0', '0%',
    'Niagara', '9', '0', '0%',
    'Oneida', '4', '0', '0%',
    'Ontario', '4', '0', '0%',
    'Clinton', '4', '0', '0%',
    'Herkimer', '3', '0', '0%',
    'Broome', '3', '1', '33.3%',
    'Montgomery', '3', '0', '0%',
    'Essex', '3', '0', '0%',
    'Wayne', '3', '0', '0%',
    'Greene', '2', '0', '0%',
    'Allegany', '2', '0', '0%',
    'Wyoming', '2', '0', '0%',
    'Hamilton', '2', '0', '0%',
    'Chenango', '2', '0', '0%',
    'Steuben', '2', '0', '0%',
    'Livingston', '2', '0', '0%',
    'Cortland', '2', '0', '0%',
    'Oswego', '+2', '2', '0', '0%',
    'Chemung', '+2', '2', '0', '0%',
    'Delaware', '1', '0', '0%',
    'Tioga', '1', '0', '0%',
    'Genesee', '1', '0', '0%',
    'Warren', '1', '0', '0%',
    'Washington', '1', '0', '0%',
    'Schoharie', '1', '0', '0%',
    'Fulton', '1', '0', '0%',
    'Jefferson', '1', '0', '0%'
]

class TestParse(unittest.TestCase):
    def test_parse(self):
        """A subset of the sample data, to make visualization, and manually creating `want`, easy."""

        # Should represent counties that did see an increase ('+NNN' after county name) and
        # some that did not see an increase ('NNN' cases after county name)
        data = [
            'New York', '+1534', '9654', '+3', '63', '0.7%',
            'Nassau', '+666', '1900', '4', '0.2%',
            'Westchester', '+486', '1873', '0', '0%',
            'Suffolk', '+372', '1034', '+3', '12', '1.2%',
            'Rockland', '+193', '455', '1', '0.2%',
            'Orange', '+84', '247', '0', '0%',
            'Albany', '+35', '123', '0', '0%',
            'Schenectady', '32', '0', '0%',
            'Putnam', '31', '0', '0%',
        ]

        want = {
            'New York': [9654, 63],
            'Nassau': [1900, 4],
            'Westchester': [1873, 0],
            'Suffolk': [1034, 12],
            'Rockland': [455, 1],
            'Orange': [247, 0],
            'Albany': [123, 0],
            'Schenectady': [32, 0],
            'Putnam': [31, 0],
        }

        m = {}
        m['New York'] = {}
        got = extract_counties_and_cases(data, m['New York'])

        self.assertEqual(got, want)

        # print(extract_counties_and_cases(DATA, m['New York']))

if __name__ == '__main__':
    unittest.main()
