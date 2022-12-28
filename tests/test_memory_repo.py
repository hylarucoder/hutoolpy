from __future__ import annotations
import unittest

from hutoolpy.memory_repo import MemoryRepo

from typing import Optional

from pydantic import BaseModel


class FriendsModel(BaseModel):
    id: int
    name: Optional[str]
    gender: Optional[str]


class AccountModel(BaseModel):
    id: int
    active: Optional[bool]
    age: Optional[int]
    name: Optional[str]
    gender: Optional[str]
    company: Optional[str]
    email: Optional[str]
    address: Optional[str]
    registered: Optional[str]

    friends: Optional[FriendsModel]


ACCOUNTS_DICT = [
    {
        "id": 0,
        "active": True,
        "age": 22,
        "name": "Angeline Holloway",
        "gender": "male",
        "company": "MEMORA",
        "email": "angelineholloway@memora.com",
        "address": "988 Kiely Place, London, Palau, 4460",
        "registered": "2014-09-21T04:35:42 -01:00",
        "friends": {"id": 0, "name": "Rivas Snow", "gender": "male"},
    },
    {
        "id": 1,
        "active": True,
        "age": 30,
        "name": "Claire Burris",
        "gender": "female",
        "company": "EXOVENT",
        "email": "claireburris@exovent.com",
        "address": "863 Senator Street, Troy, Puerto Rico, 4092",
        "registered": "2015-11-15T09:38:43 -00:00",
        "friends": {"id": 1, "name": "Marta Walton", "gender": "female"},
    },
    {
        "id": 2,
        "active": True,
        "age": 22,
        "name": "Jeannette Clarke",
        "gender": "female",
        "company": "FITCORE",
        "email": "jeannetteclarke@fitcore.com",
        "address": "248 Village Road, Brecon, Hawaii, 5992",
        "registered": "2015-05-02T05:44:45 -01:00",
        "friends": {"id": 2, "name": "Schultz Nielsen", "gender": "male"},
    },
    {
        "id": 3,
        "active": False,
        "age": 35,
        "name": "Zimmerman Mosley",
        "gender": "female",
        "company": "GAZAK",
        "email": "zimmermanmosley@gazak.com",
        "address": "114 Elliott Place, Watchtower, Kansas, 888",
        "registered": "2015-01-24T04:58:59 -00:00",
        "friends": {"id": 3, "name": "Figueroa Melton", "gender": "male"},
    },
    {
        "id": 4,
        "active": False,
        "age": 22,
        "name": "Montgomery Bolton",
        "gender": "male",
        "company": "KOFFEE",
        "email": "montgomerybolton@koffee.com",
        "address": "167 Dennett Place, Trail, Idaho, 5066",
        "registered": "2015-03-09T03:03:53 -00:00",
        "friends": {"id": 4, "name": "Jacklyn Stein", "gender": "female"},
    },
    {
        "id": 5,
        "active": True,
        "age": 24,
        "name": "Petty Lang",
        "gender": "male",
        "company": "GOLISTIC",
        "email": "pettylang@golistic.com",
        "address": "921 Montgomery Street, Manchester, Oregon, 4267",
        "registered": "2014-05-01T09:13:11 -01:00",
        "friends": {"id": 5, "name": "Aurelia Tyson", "gender": "female"},
    },
    {
        "id": 6,
        "active": True,
        "age": 32,
        "name": "Ward Waller",
        "gender": "male",
        "company": "ELITA",
        "email": "wardwaller@elita.com",
        "address": "849 Stuart Street, Grandview, South Dakota, 2509",
        "registered": "2015-12-08T06:01:21 -00:00",
        "friends": {"id": 6, "name": "Wong Dunn", "gender": "male"},
    },
    {
        "id": 7,
        "active": False,
        "age": 20,
        "name": "Crawford Wilkins",
        "gender": "male",
        "company": "VICON",
        "email": "crawfordwilkins@vicon.com",
        "address": "814 Lawrence Avenue, Finzel, California, 7246",
        "registered": "2016-04-06T06:47:57 -01:00",
        "friends": {"id": 7, "name": "Lindsay Joseph", "gender": "female"},
    },
]

ACCOUNT_MODELS = [AccountModel(**_) for _ in ACCOUNTS_DICT]


class TestQueries(unittest.TestCase):
    def setUp(self):
        self.repo = MemoryRepo(ACCOUNT_MODELS)

    def test_filters_lamda(self):
        self.assertEqual(
            self.repo.filter(company=lambda x: x == "VICON" or x == "ELITA").count(),
            2,
        )
        self.assertEqual(self.repo.filter(age=lambda x: x >= 20 and x <= 30).count(), 6)
        self.assertEqual(
            self.repo.filter(age=lambda x: x >= 20 and x <= 30).exclude(gender="male").count(),
            2,
        )
        self.assertEqual(
            self.repo.filter(age=lambda x: x >= 20 and x <= 30).exclude(gender="female").count(),
            4,
        )

    def test_filters(self):
        self.assertEqual(self.repo.filter(name="Crawford Wilkins")[0].id, ACCOUNT_MODELS[7].id)
        self.assertEqual(
            self.repo.filter(address__icontains="London")[0].id,
            ACCOUNT_MODELS[0].id,
        )
        self.assertEqual(self.repo.filter(email="crawfordwilkins@vicon.com").count(), 1)
        self.assertEqual(self.repo.filter(active=True).count(), 5)
        self.assertEqual(self.repo.filter(active=False).count(), 3)
        self.assertEqual(self.repo.filter(gender="male").count(), 5)
        self.assertEqual(self.repo.filter(gender="female").count(), 3)
        self.assertEqual(self.repo.filter(address__contains="london").count(), 0)
        self.assertEqual(self.repo.filter(address__icontains="London").count(), 1)
        self.assertEqual(self.repo.filter(age__gte=30).count(), 3)
        self.assertEqual(self.repo.filter(age__gt=30).count(), 2)
        self.assertEqual(self.repo.filter(age__lte=22).count(), 4)
        self.assertEqual(self.repo.filter(age__lt=30).count(), 5)
        self.assertEqual(self.repo.filter(age__lte=30).count(), 6)
        self.assertEqual(self.repo.filter(name__startswith="Angeline").count(), 1)
        self.assertEqual(self.repo.filter(name__startswith="c").count(), 0)
        self.assertEqual(self.repo.filter(name__istartswith="c").count(), 2)
        self.assertEqual(self.repo.filter(name__istartswith="c").count(), 2)
        self.assertEqual(self.repo.filter(name__endswith="s").count(), 2)

    def test_filters_combine(self):
        self.assertEqual(
            self.repo.filter(active=True, age__lte=22, gender="female", company="FITCORE").count(),
            1,
        )
        self.assertEqual(self.repo.filter(active=True, age__lte=22, gender="female").count(), 1)
        self.assertEqual(self.repo.filter(active=True, age=22, gender="female").count(), 1)
        self.assertEqual(self.repo.filter(active=True, age=22, gender="male").count(), 1)
        self.assertEqual(
            self.repo.filter(active=True, age=22, gender="male", name="Angeline Holloway").count(),
            1,
        )
        self.assertEqual(self.repo.filter(active=True, id=5).count(), 1)
        self.assertEqual(self.repo.filter(active=True, age=22).count(), 2)
        self.assertEqual(self.repo.filter(active=True, id=5).first().id, ACCOUNT_MODELS[5].id)

    def test_filters_combine_chained(self):
        self.assertEqual(
            self.repo.filter(active=True).filter(age__lte=22).filter(gender="female").filter(company="FITCORE").count(),
            1,
        )
        self.assertEqual(
            self.repo.filter(active=True).filter(age__lte=22).filter(gender="female").count(),
            1,
        )
        self.assertEqual(
            self.repo.filter(active=True).filter(age=22).filter(gender="female").count(),
            1,
        )
        self.assertEqual(
            self.repo.filter(active=True).filter(age=22).filter(gender="male").count(),
            1,
        )
        self.assertEqual(
            self.repo.filter(active=True).filter(age=22).filter(gender="male").filter(name="Angeline Holloway").count(),
            1,
        )
        self.assertEqual(self.repo.filter(active=True).filter(id=5).count(), 1)
        self.assertEqual(self.repo.filter(active=True).filter(age=22).count(), 2)
        self.assertEqual(
            self.repo.filter(active=True).filter(id=5).first().id,
            ACCOUNT_MODELS[5].id,
        )

    def test_exclude(self):
        self.assertEqual(self.repo.exclude(email="crawfordwilkins@vicon.com").count(), 7)
        self.assertEqual(self.repo.exclude(gender="male").count(), 3)
        self.assertEqual(self.repo.exclude(active=True).count(), 3)
        self.assertEqual(self.repo.exclude(active=False).count(), 5)
        self.assertEqual(self.repo.exclude(address__contains="london").count(), 8)
        self.assertEqual(self.repo.exclude(address__icontains="London").count(), 7)
        self.assertEqual(self.repo.exclude(age__gte=30).count(), 5)
        self.assertEqual(self.repo.exclude(age__gt=30).count(), 6)
        self.assertEqual(self.repo.exclude(age__lte=22).count(), 4)
        self.assertEqual(self.repo.exclude(age__lt=30).count(), 3)
        self.assertEqual(self.repo.exclude(age__lte=30).count(), 2)
        self.assertEqual(self.repo.exclude(name__startswith="Angeline").count(), 7)
        self.assertEqual(self.repo.exclude(name__startswith="c").count(), 8)
        self.assertEqual(self.repo.exclude(name__istartswith="c").count(), 6)
        self.assertEqual(self.repo.exclude(name__istartswith="c").count(), 6)
        self.assertEqual(self.repo.exclude(name__endswith="s").count(), 6)

    def test_exclude_combine(self):
        self.assertEqual(self.repo.exclude(active=True, age__lte=22, gender="female").count(), 7)
        self.assertEqual(self.repo.exclude(active=True, age=22, gender="female").count(), 7)
        self.assertEqual(self.repo.exclude(active=True, id=5).count(), 7)
        self.assertEqual(self.repo.exclude(active=True, age=22).count(), 6)

    def test_exclude_combine_chained(self):
        self.assertEqual(
            self.repo.exclude(active=True).exclude(age__lte=22).exclude(gender="male").count(),
            1,
        )
        self.assertEqual(
            self.repo.exclude(active=True).exclude(age=22).exclude(gender="female").count(),
            1,
        )
        self.assertEqual(self.repo.exclude(active=True).exclude(id=5).count(), 3)
        self.assertEqual(self.repo.exclude(active=True).exclude(age=22).count(), 2)

    def test_filter_combined_with_exclude(self):
        self.assertEqual(self.repo.filter(active=True).exclude(gender="male").count(), 2)
        self.assertEqual(
            self.repo.filter(active=True, gender="male").exclude(age__lte=22).count(),
            2,
        )

    def test_get(self):
        self.assertEqual(self.repo.get(name="Angeline Holloway"), ACCOUNT_MODELS[0])
        self.assertEqual(self.repo.get(id=0), ACCOUNT_MODELS[0])

    def test_related_lookups(self):
        self.assertEqual(self.repo.filter(friends__gender="male").count(), 4)
        self.assertEqual(self.repo.filter(friends__gender="female").count(), 4)
        self.assertEqual(
            self.repo.filter(friends__gender="male").exclude(active=False).count(),
            3,
        )
        self.assertEqual(self.repo.filter(friends__gender="male").exclude(active=True).count(), 1)

    def test_ordering(self):
        self.assertEqual(list(self.repo.order_by("id")), ACCOUNT_MODELS)
        self.assertEqual(list(self.repo.order_by("-id")), list(reversed(ACCOUNT_MODELS)))
        self.assertEqual(
            list(self.repo.order_by("gender")),
            sorted(ACCOUNT_MODELS, key=lambda x: x.gender),
        )
        self.assertEqual(
            list(self.repo.order_by("-gender")),
            sorted(ACCOUNT_MODELS, key=lambda x: x.gender, reverse=True),
        )

    def test_orderings(self):
        self.assertEqual(
            list(self.repo.order_by("friends__gender")),
            sorted(ACCOUNT_MODELS, key=lambda x: x.friends.gender),
        )
        self.assertEqual(
            list(self.repo.order_by("-friends__gender")),
            sorted(ACCOUNT_MODELS, key=lambda x: x.friends.gender, reverse=True),
        )

        self.assertEqual(
            list(self.repo.order_by("friends__name")),
            sorted(ACCOUNT_MODELS, key=lambda x: x.friends.name),
        )
        self.assertEqual(
            list(self.repo.order_by("-friends__name")),
            sorted(ACCOUNT_MODELS, key=lambda x: x.friends.name, reverse=True),
        )

    def test_exists(self):
        self.assertTrue(self.repo.filter(email="wardwaller@elita.com").exists())
        self.assertFalse(self.repo.filter(email="said.ali@msn.com").exists())
        self.assertTrue(self.repo.filter(friends__name="Lindsay Joseph").exists())
        self.assertFalse(self.repo.filter(friends__name="Said Ali").exists())

    def test_first(self):
        self.assertTrue(self.repo.filter(email="wardwaller@elita.com").first())
        self.assertFalse(self.repo.filter(email="said.ali@msn.com").first())
        self.assertEqual(
            self.repo.filter(email="wardwaller@elita.com").first(),
            self.repo.filter(email="wardwaller@elita.com")[0],
        )

    def test_range(self):
        queryset = self.repo.filter(registered__range=("2015-09-21", "2016-12-08")).exclude(name="Crawford Wilkins")
        self.assertEqual(queryset.count(), 2)

        queryset = self.repo.filter(registered__range=("2015-11-15", "2015-11-16"))
        self.assertEqual(queryset[0].id, ACCOUNT_MODELS[1].id)

    def test_as_dict(self):
        d = (
            self.repo.filter(registered__range=("2015-09-21", "2016-12-08"))
            .exclude(name="Crawford Wilkins")
            .as_dict("id", "age")
        )
        assert (
            d[
                (
                    1,
                    30,
                )
            ]
            == ACCOUNT_MODELS[1]
        )
