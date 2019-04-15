# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Department as DepartmentModel, Employee as EmployeeModel, Inventory as InventoryModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class DepartmentConnection(relay.Connection):
    class Meta:
        node = Department


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class EmployeConnection(relay.Connection):
    class Meta:
        node = Employee

class Inventory(SQLAlchemyObjectType):
    class Meta:
        model = InventoryModel
        interfaces = (relay.Node, )


class InventoryConnection(relay.Connection):
    class Meta:
        node = Inventory

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_products = SQLAlchemyConnectionField(InventoryConnection)
    all_employees = SQLAlchemyConnectionField(EmployeConnection)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(DepartmentConnection, sort=None)

schema = graphene.Schema(query=Query)