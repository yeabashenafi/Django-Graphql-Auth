import graphene

from graphql_auth.schema import UserQuery, MeQuery

class Query(UserQuery,MemoryError,graphene.ObjectType):
    pass
 
schema = graphene.Schema(query=Query)