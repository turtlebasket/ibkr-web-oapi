from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_w8imy_box_11_status import FormW8IMYBox11Status
from ..models.form_w8imy_entity_type import FormW8IMYEntityType
from ..models.form_w8imy_fatca_status import FormW8IMYFatcaStatus
from ..models.form_w8imy_us_tin_type import FormW8IMYUsTinType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormW8IMY")


@_attrs_define
class FormW8IMY:
    """
    Attributes:
        name (Union[Unset, str]):
        country_of_incorporation (Union[Unset, str]):
        disregarded_entity_name (Union[Unset, str]):
        entity_type (Union[Unset, FormW8IMYEntityType]):
        fatca_status (Union[Unset, FormW8IMYFatcaStatus]):
        us_tin (Union[Unset, str]):
        us_tin_type (Union[Unset, FormW8IMYUsTinType]):
        giin (Union[Unset, str]):
        reference_number (Union[Unset, int]):
        box_11_status (Union[Unset, FormW8IMYBox11Status]):
        part_314a (Union[Unset, bool]):
        part_314b (Union[Unset, bool]):
        part_314c (Union[Unset, bool]):
        part_314c_desc (Union[Unset, str]):
        part_314d (Union[Unset, bool]):
        part_314d_desc (Union[Unset, str]):
        part_314e (Union[Unset, bool]):
        part_314e_desc (Union[Unset, str]):
        part_314ei (Union[Unset, bool]):
        part_314e_ii (Union[Unset, bool]):
        part_415a (Union[Unset, bool]):
        part_415b (Union[Unset, bool]):
        part_415c (Union[Unset, bool]):
        part_415d (Union[Unset, bool]):
        part_516a (Union[Unset, bool]):
        part_516b (Union[Unset, bool]):
        part_516c (Union[Unset, bool]):
        part_617a (Union[Unset, bool]):
        part_617b (Union[Unset, bool]):
        part_617c (Union[Unset, bool]):
        part718 (Union[Unset, bool]):
        part819 (Union[Unset, bool]):
        part920 (Union[Unset, bool]):
        part1021 (Union[Unset, str]):
        part_1021a (Union[Unset, str]):
        part_1021b (Union[Unset, bool]):
        part_1021c (Union[Unset, bool]):
        part_1122a (Union[Unset, bool]):
        part_1122b (Union[Unset, bool]):
        part_1122c (Union[Unset, bool]):
        part1223 (Union[Unset, bool]):
        part1324 (Union[Unset, bool]):
        part_1425a (Union[Unset, str]):
        part_1425b (Union[Unset, bool]):
        part1526 (Union[Unset, bool]):
        part_1627a (Union[Unset, bool]):
        part_1627b (Union[Unset, bool]):
        part_1627c (Union[Unset, bool]):
        part1728 (Union[Unset, bool]):
        part1829 (Union[Unset, bool]):
        part_1829_desc_1 (Union[Unset, str]):
        part_1829_desc_2 (Union[Unset, str]):
        part_1829_desc_3 (Union[Unset, str]):
        part_1930a (Union[Unset, bool]):
        part_1930b (Union[Unset, bool]):
        part_1930c (Union[Unset, bool]):
        part_1930d (Union[Unset, bool]):
        part_1930e (Union[Unset, bool]):
        part_1930f (Union[Unset, bool]):
        part2031 (Union[Unset, bool]):
        part2132 (Union[Unset, bool]):
        part_2132_desc (Union[Unset, str]):
        part2233 (Union[Unset, bool]):
        part_2233_desc (Union[Unset, str]):
        part_2334a (Union[Unset, bool]):
        part_2334a_desc (Union[Unset, str]):
        part_2334b (Union[Unset, bool]):
        part_2334b_desc (Union[Unset, str]):
        part2435 (Union[Unset, bool]):
        part2536 (Union[Unset, bool]):
        part2637 (Union[Unset, bool]):
        part2738 (Union[Unset, str]):
        part2739 (Union[Unset, bool]):
        cert (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    country_of_incorporation: Union[Unset, str] = UNSET
    disregarded_entity_name: Union[Unset, str] = UNSET
    entity_type: Union[Unset, FormW8IMYEntityType] = UNSET
    fatca_status: Union[Unset, FormW8IMYFatcaStatus] = UNSET
    us_tin: Union[Unset, str] = UNSET
    us_tin_type: Union[Unset, FormW8IMYUsTinType] = UNSET
    giin: Union[Unset, str] = UNSET
    reference_number: Union[Unset, int] = UNSET
    box_11_status: Union[Unset, FormW8IMYBox11Status] = UNSET
    part_314a: Union[Unset, bool] = UNSET
    part_314b: Union[Unset, bool] = UNSET
    part_314c: Union[Unset, bool] = UNSET
    part_314c_desc: Union[Unset, str] = UNSET
    part_314d: Union[Unset, bool] = UNSET
    part_314d_desc: Union[Unset, str] = UNSET
    part_314e: Union[Unset, bool] = UNSET
    part_314e_desc: Union[Unset, str] = UNSET
    part_314ei: Union[Unset, bool] = UNSET
    part_314e_ii: Union[Unset, bool] = UNSET
    part_415a: Union[Unset, bool] = UNSET
    part_415b: Union[Unset, bool] = UNSET
    part_415c: Union[Unset, bool] = UNSET
    part_415d: Union[Unset, bool] = UNSET
    part_516a: Union[Unset, bool] = UNSET
    part_516b: Union[Unset, bool] = UNSET
    part_516c: Union[Unset, bool] = UNSET
    part_617a: Union[Unset, bool] = UNSET
    part_617b: Union[Unset, bool] = UNSET
    part_617c: Union[Unset, bool] = UNSET
    part718: Union[Unset, bool] = UNSET
    part819: Union[Unset, bool] = UNSET
    part920: Union[Unset, bool] = UNSET
    part1021: Union[Unset, str] = UNSET
    part_1021a: Union[Unset, str] = UNSET
    part_1021b: Union[Unset, bool] = UNSET
    part_1021c: Union[Unset, bool] = UNSET
    part_1122a: Union[Unset, bool] = UNSET
    part_1122b: Union[Unset, bool] = UNSET
    part_1122c: Union[Unset, bool] = UNSET
    part1223: Union[Unset, bool] = UNSET
    part1324: Union[Unset, bool] = UNSET
    part_1425a: Union[Unset, str] = UNSET
    part_1425b: Union[Unset, bool] = UNSET
    part1526: Union[Unset, bool] = UNSET
    part_1627a: Union[Unset, bool] = UNSET
    part_1627b: Union[Unset, bool] = UNSET
    part_1627c: Union[Unset, bool] = UNSET
    part1728: Union[Unset, bool] = UNSET
    part1829: Union[Unset, bool] = UNSET
    part_1829_desc_1: Union[Unset, str] = UNSET
    part_1829_desc_2: Union[Unset, str] = UNSET
    part_1829_desc_3: Union[Unset, str] = UNSET
    part_1930a: Union[Unset, bool] = UNSET
    part_1930b: Union[Unset, bool] = UNSET
    part_1930c: Union[Unset, bool] = UNSET
    part_1930d: Union[Unset, bool] = UNSET
    part_1930e: Union[Unset, bool] = UNSET
    part_1930f: Union[Unset, bool] = UNSET
    part2031: Union[Unset, bool] = UNSET
    part2132: Union[Unset, bool] = UNSET
    part_2132_desc: Union[Unset, str] = UNSET
    part2233: Union[Unset, bool] = UNSET
    part_2233_desc: Union[Unset, str] = UNSET
    part_2334a: Union[Unset, bool] = UNSET
    part_2334a_desc: Union[Unset, str] = UNSET
    part_2334b: Union[Unset, bool] = UNSET
    part_2334b_desc: Union[Unset, str] = UNSET
    part2435: Union[Unset, bool] = UNSET
    part2536: Union[Unset, bool] = UNSET
    part2637: Union[Unset, bool] = UNSET
    part2738: Union[Unset, str] = UNSET
    part2739: Union[Unset, bool] = UNSET
    cert: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        country_of_incorporation = self.country_of_incorporation

        disregarded_entity_name = self.disregarded_entity_name

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        fatca_status: Union[Unset, str] = UNSET
        if not isinstance(self.fatca_status, Unset):
            fatca_status = self.fatca_status.value

        us_tin = self.us_tin

        us_tin_type: Union[Unset, str] = UNSET
        if not isinstance(self.us_tin_type, Unset):
            us_tin_type = self.us_tin_type.value

        giin = self.giin

        reference_number = self.reference_number

        box_11_status: Union[Unset, str] = UNSET
        if not isinstance(self.box_11_status, Unset):
            box_11_status = self.box_11_status.value

        part_314a = self.part_314a

        part_314b = self.part_314b

        part_314c = self.part_314c

        part_314c_desc = self.part_314c_desc

        part_314d = self.part_314d

        part_314d_desc = self.part_314d_desc

        part_314e = self.part_314e

        part_314e_desc = self.part_314e_desc

        part_314ei = self.part_314ei

        part_314e_ii = self.part_314e_ii

        part_415a = self.part_415a

        part_415b = self.part_415b

        part_415c = self.part_415c

        part_415d = self.part_415d

        part_516a = self.part_516a

        part_516b = self.part_516b

        part_516c = self.part_516c

        part_617a = self.part_617a

        part_617b = self.part_617b

        part_617c = self.part_617c

        part718 = self.part718

        part819 = self.part819

        part920 = self.part920

        part1021 = self.part1021

        part_1021a = self.part_1021a

        part_1021b = self.part_1021b

        part_1021c = self.part_1021c

        part_1122a = self.part_1122a

        part_1122b = self.part_1122b

        part_1122c = self.part_1122c

        part1223 = self.part1223

        part1324 = self.part1324

        part_1425a = self.part_1425a

        part_1425b = self.part_1425b

        part1526 = self.part1526

        part_1627a = self.part_1627a

        part_1627b = self.part_1627b

        part_1627c = self.part_1627c

        part1728 = self.part1728

        part1829 = self.part1829

        part_1829_desc_1 = self.part_1829_desc_1

        part_1829_desc_2 = self.part_1829_desc_2

        part_1829_desc_3 = self.part_1829_desc_3

        part_1930a = self.part_1930a

        part_1930b = self.part_1930b

        part_1930c = self.part_1930c

        part_1930d = self.part_1930d

        part_1930e = self.part_1930e

        part_1930f = self.part_1930f

        part2031 = self.part2031

        part2132 = self.part2132

        part_2132_desc = self.part_2132_desc

        part2233 = self.part2233

        part_2233_desc = self.part_2233_desc

        part_2334a = self.part_2334a

        part_2334a_desc = self.part_2334a_desc

        part_2334b = self.part_2334b

        part_2334b_desc = self.part_2334b_desc

        part2435 = self.part2435

        part2536 = self.part2536

        part2637 = self.part2637

        part2738 = self.part2738

        part2739 = self.part2739

        cert = self.cert

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if country_of_incorporation is not UNSET:
            field_dict["countryOfIncorporation"] = country_of_incorporation
        if disregarded_entity_name is not UNSET:
            field_dict["disregardedEntityName"] = disregarded_entity_name
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if fatca_status is not UNSET:
            field_dict["fatcaStatus"] = fatca_status
        if us_tin is not UNSET:
            field_dict["usTin"] = us_tin
        if us_tin_type is not UNSET:
            field_dict["usTinType"] = us_tin_type
        if giin is not UNSET:
            field_dict["giin"] = giin
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if box_11_status is not UNSET:
            field_dict["box11Status"] = box_11_status
        if part_314a is not UNSET:
            field_dict["part314A"] = part_314a
        if part_314b is not UNSET:
            field_dict["part314B"] = part_314b
        if part_314c is not UNSET:
            field_dict["part314C"] = part_314c
        if part_314c_desc is not UNSET:
            field_dict["part314CDesc"] = part_314c_desc
        if part_314d is not UNSET:
            field_dict["part314D"] = part_314d
        if part_314d_desc is not UNSET:
            field_dict["part314DDesc"] = part_314d_desc
        if part_314e is not UNSET:
            field_dict["part314E"] = part_314e
        if part_314e_desc is not UNSET:
            field_dict["part314EDesc"] = part_314e_desc
        if part_314ei is not UNSET:
            field_dict["part314EI"] = part_314ei
        if part_314e_ii is not UNSET:
            field_dict["part314EIi"] = part_314e_ii
        if part_415a is not UNSET:
            field_dict["part415A"] = part_415a
        if part_415b is not UNSET:
            field_dict["part415B"] = part_415b
        if part_415c is not UNSET:
            field_dict["part415C"] = part_415c
        if part_415d is not UNSET:
            field_dict["part415D"] = part_415d
        if part_516a is not UNSET:
            field_dict["part516A"] = part_516a
        if part_516b is not UNSET:
            field_dict["part516B"] = part_516b
        if part_516c is not UNSET:
            field_dict["part516C"] = part_516c
        if part_617a is not UNSET:
            field_dict["part617A"] = part_617a
        if part_617b is not UNSET:
            field_dict["part617B"] = part_617b
        if part_617c is not UNSET:
            field_dict["part617C"] = part_617c
        if part718 is not UNSET:
            field_dict["part718"] = part718
        if part819 is not UNSET:
            field_dict["part819"] = part819
        if part920 is not UNSET:
            field_dict["part920"] = part920
        if part1021 is not UNSET:
            field_dict["part1021"] = part1021
        if part_1021a is not UNSET:
            field_dict["part1021A"] = part_1021a
        if part_1021b is not UNSET:
            field_dict["part1021B"] = part_1021b
        if part_1021c is not UNSET:
            field_dict["part1021C"] = part_1021c
        if part_1122a is not UNSET:
            field_dict["part1122A"] = part_1122a
        if part_1122b is not UNSET:
            field_dict["part1122B"] = part_1122b
        if part_1122c is not UNSET:
            field_dict["part1122C"] = part_1122c
        if part1223 is not UNSET:
            field_dict["part1223"] = part1223
        if part1324 is not UNSET:
            field_dict["part1324"] = part1324
        if part_1425a is not UNSET:
            field_dict["part1425A"] = part_1425a
        if part_1425b is not UNSET:
            field_dict["part1425B"] = part_1425b
        if part1526 is not UNSET:
            field_dict["part1526"] = part1526
        if part_1627a is not UNSET:
            field_dict["part1627A"] = part_1627a
        if part_1627b is not UNSET:
            field_dict["part1627B"] = part_1627b
        if part_1627c is not UNSET:
            field_dict["part1627C"] = part_1627c
        if part1728 is not UNSET:
            field_dict["part1728"] = part1728
        if part1829 is not UNSET:
            field_dict["part1829"] = part1829
        if part_1829_desc_1 is not UNSET:
            field_dict["part1829Desc1"] = part_1829_desc_1
        if part_1829_desc_2 is not UNSET:
            field_dict["part1829Desc2"] = part_1829_desc_2
        if part_1829_desc_3 is not UNSET:
            field_dict["part1829Desc3"] = part_1829_desc_3
        if part_1930a is not UNSET:
            field_dict["part1930A"] = part_1930a
        if part_1930b is not UNSET:
            field_dict["part1930B"] = part_1930b
        if part_1930c is not UNSET:
            field_dict["part1930C"] = part_1930c
        if part_1930d is not UNSET:
            field_dict["part1930D"] = part_1930d
        if part_1930e is not UNSET:
            field_dict["part1930E"] = part_1930e
        if part_1930f is not UNSET:
            field_dict["part1930F"] = part_1930f
        if part2031 is not UNSET:
            field_dict["part2031"] = part2031
        if part2132 is not UNSET:
            field_dict["part2132"] = part2132
        if part_2132_desc is not UNSET:
            field_dict["part2132Desc"] = part_2132_desc
        if part2233 is not UNSET:
            field_dict["part2233"] = part2233
        if part_2233_desc is not UNSET:
            field_dict["part2233Desc"] = part_2233_desc
        if part_2334a is not UNSET:
            field_dict["part2334A"] = part_2334a
        if part_2334a_desc is not UNSET:
            field_dict["part2334ADesc"] = part_2334a_desc
        if part_2334b is not UNSET:
            field_dict["part2334B"] = part_2334b
        if part_2334b_desc is not UNSET:
            field_dict["part2334BDesc"] = part_2334b_desc
        if part2435 is not UNSET:
            field_dict["part2435"] = part2435
        if part2536 is not UNSET:
            field_dict["part2536"] = part2536
        if part2637 is not UNSET:
            field_dict["part2637"] = part2637
        if part2738 is not UNSET:
            field_dict["part2738"] = part2738
        if part2739 is not UNSET:
            field_dict["part2739"] = part2739
        if cert is not UNSET:
            field_dict["cert"] = cert

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        country_of_incorporation = d.pop("countryOfIncorporation", UNSET)

        disregarded_entity_name = d.pop("disregardedEntityName", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, FormW8IMYEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = FormW8IMYEntityType(_entity_type)

        _fatca_status = d.pop("fatcaStatus", UNSET)
        fatca_status: Union[Unset, FormW8IMYFatcaStatus]
        if isinstance(_fatca_status, Unset):
            fatca_status = UNSET
        else:
            fatca_status = FormW8IMYFatcaStatus(_fatca_status)

        us_tin = d.pop("usTin", UNSET)

        _us_tin_type = d.pop("usTinType", UNSET)
        us_tin_type: Union[Unset, FormW8IMYUsTinType]
        if isinstance(_us_tin_type, Unset):
            us_tin_type = UNSET
        else:
            us_tin_type = FormW8IMYUsTinType(_us_tin_type)

        giin = d.pop("giin", UNSET)

        reference_number = d.pop("referenceNumber", UNSET)

        _box_11_status = d.pop("box11Status", UNSET)
        box_11_status: Union[Unset, FormW8IMYBox11Status]
        if isinstance(_box_11_status, Unset):
            box_11_status = UNSET
        else:
            box_11_status = FormW8IMYBox11Status(_box_11_status)

        part_314a = d.pop("part314A", UNSET)

        part_314b = d.pop("part314B", UNSET)

        part_314c = d.pop("part314C", UNSET)

        part_314c_desc = d.pop("part314CDesc", UNSET)

        part_314d = d.pop("part314D", UNSET)

        part_314d_desc = d.pop("part314DDesc", UNSET)

        part_314e = d.pop("part314E", UNSET)

        part_314e_desc = d.pop("part314EDesc", UNSET)

        part_314ei = d.pop("part314EI", UNSET)

        part_314e_ii = d.pop("part314EIi", UNSET)

        part_415a = d.pop("part415A", UNSET)

        part_415b = d.pop("part415B", UNSET)

        part_415c = d.pop("part415C", UNSET)

        part_415d = d.pop("part415D", UNSET)

        part_516a = d.pop("part516A", UNSET)

        part_516b = d.pop("part516B", UNSET)

        part_516c = d.pop("part516C", UNSET)

        part_617a = d.pop("part617A", UNSET)

        part_617b = d.pop("part617B", UNSET)

        part_617c = d.pop("part617C", UNSET)

        part718 = d.pop("part718", UNSET)

        part819 = d.pop("part819", UNSET)

        part920 = d.pop("part920", UNSET)

        part1021 = d.pop("part1021", UNSET)

        part_1021a = d.pop("part1021A", UNSET)

        part_1021b = d.pop("part1021B", UNSET)

        part_1021c = d.pop("part1021C", UNSET)

        part_1122a = d.pop("part1122A", UNSET)

        part_1122b = d.pop("part1122B", UNSET)

        part_1122c = d.pop("part1122C", UNSET)

        part1223 = d.pop("part1223", UNSET)

        part1324 = d.pop("part1324", UNSET)

        part_1425a = d.pop("part1425A", UNSET)

        part_1425b = d.pop("part1425B", UNSET)

        part1526 = d.pop("part1526", UNSET)

        part_1627a = d.pop("part1627A", UNSET)

        part_1627b = d.pop("part1627B", UNSET)

        part_1627c = d.pop("part1627C", UNSET)

        part1728 = d.pop("part1728", UNSET)

        part1829 = d.pop("part1829", UNSET)

        part_1829_desc_1 = d.pop("part1829Desc1", UNSET)

        part_1829_desc_2 = d.pop("part1829Desc2", UNSET)

        part_1829_desc_3 = d.pop("part1829Desc3", UNSET)

        part_1930a = d.pop("part1930A", UNSET)

        part_1930b = d.pop("part1930B", UNSET)

        part_1930c = d.pop("part1930C", UNSET)

        part_1930d = d.pop("part1930D", UNSET)

        part_1930e = d.pop("part1930E", UNSET)

        part_1930f = d.pop("part1930F", UNSET)

        part2031 = d.pop("part2031", UNSET)

        part2132 = d.pop("part2132", UNSET)

        part_2132_desc = d.pop("part2132Desc", UNSET)

        part2233 = d.pop("part2233", UNSET)

        part_2233_desc = d.pop("part2233Desc", UNSET)

        part_2334a = d.pop("part2334A", UNSET)

        part_2334a_desc = d.pop("part2334ADesc", UNSET)

        part_2334b = d.pop("part2334B", UNSET)

        part_2334b_desc = d.pop("part2334BDesc", UNSET)

        part2435 = d.pop("part2435", UNSET)

        part2536 = d.pop("part2536", UNSET)

        part2637 = d.pop("part2637", UNSET)

        part2738 = d.pop("part2738", UNSET)

        part2739 = d.pop("part2739", UNSET)

        cert = d.pop("cert", UNSET)

        form_w8imy = cls(
            name=name,
            country_of_incorporation=country_of_incorporation,
            disregarded_entity_name=disregarded_entity_name,
            entity_type=entity_type,
            fatca_status=fatca_status,
            us_tin=us_tin,
            us_tin_type=us_tin_type,
            giin=giin,
            reference_number=reference_number,
            box_11_status=box_11_status,
            part_314a=part_314a,
            part_314b=part_314b,
            part_314c=part_314c,
            part_314c_desc=part_314c_desc,
            part_314d=part_314d,
            part_314d_desc=part_314d_desc,
            part_314e=part_314e,
            part_314e_desc=part_314e_desc,
            part_314ei=part_314ei,
            part_314e_ii=part_314e_ii,
            part_415a=part_415a,
            part_415b=part_415b,
            part_415c=part_415c,
            part_415d=part_415d,
            part_516a=part_516a,
            part_516b=part_516b,
            part_516c=part_516c,
            part_617a=part_617a,
            part_617b=part_617b,
            part_617c=part_617c,
            part718=part718,
            part819=part819,
            part920=part920,
            part1021=part1021,
            part_1021a=part_1021a,
            part_1021b=part_1021b,
            part_1021c=part_1021c,
            part_1122a=part_1122a,
            part_1122b=part_1122b,
            part_1122c=part_1122c,
            part1223=part1223,
            part1324=part1324,
            part_1425a=part_1425a,
            part_1425b=part_1425b,
            part1526=part1526,
            part_1627a=part_1627a,
            part_1627b=part_1627b,
            part_1627c=part_1627c,
            part1728=part1728,
            part1829=part1829,
            part_1829_desc_1=part_1829_desc_1,
            part_1829_desc_2=part_1829_desc_2,
            part_1829_desc_3=part_1829_desc_3,
            part_1930a=part_1930a,
            part_1930b=part_1930b,
            part_1930c=part_1930c,
            part_1930d=part_1930d,
            part_1930e=part_1930e,
            part_1930f=part_1930f,
            part2031=part2031,
            part2132=part2132,
            part_2132_desc=part_2132_desc,
            part2233=part2233,
            part_2233_desc=part_2233_desc,
            part_2334a=part_2334a,
            part_2334a_desc=part_2334a_desc,
            part_2334b=part_2334b,
            part_2334b_desc=part_2334b_desc,
            part2435=part2435,
            part2536=part2536,
            part2637=part2637,
            part2738=part2738,
            part2739=part2739,
            cert=cert,
        )

        form_w8imy.additional_properties = d
        return form_w8imy

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
