from enum import Enum
from typing import Optional, List, Any, Dict
import json

class Format(Enum):
    DATE_TIME = "date-time"
    DECIMAL = "decimal"
    INT32 = "int32"


class ApRouteIDType(Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    NUMBER = "number"
    STRING = "string"


class InvoiceCountClass:
    type: ApRouteIDType
    format: Optional[Format]

    def __init__(self, type: ApRouteIDType, format: Optional[Format]) -> None:
        self.type = type
        self.format = format


class IncludeSupportingDocumentsClass:
    type: ApRouteIDType

    def __init__(self, type: ApRouteIDType) -> None:
        self.type = type


class PaymentComments:
    type: ApRouteIDType
    nullable: bool

    def __init__(self, type: ApRouteIDType, nullable: bool) -> None:
        self.type = type
        self.nullable = nullable


class FileFormatClass:
    ref: str

    def __init__(self, ref: str) -> None:
        self.ref = ref


class APBatchModelProperties:
    batch_id: IncludeSupportingDocumentsClass
    ap_route_id: InvoiceCountClass
    sent_to_ap_date_time: InvoiceCountClass
    batch_run_date_time: InvoiceCountClass
    payment_status: FileFormatClass
    payment_comments: PaymentComments

    def __init__(self, batch_id: IncludeSupportingDocumentsClass, ap_route_id: InvoiceCountClass, sent_to_ap_date_time: InvoiceCountClass, batch_run_date_time: InvoiceCountClass, payment_status: FileFormatClass, payment_comments: PaymentComments) -> None:
        self.batch_id = batch_id
        self.ap_route_id = ap_route_id
        self.sent_to_ap_date_time = sent_to_ap_date_time
        self.batch_run_date_time = batch_run_date_time
        self.payment_status = payment_status
        self.payment_comments = payment_comments


class APBatchModelType(Enum):
    BOOLEAN = "boolean"
    OBJECT = "object"


class ApBatchModel:
    title: str
    type: APBatchModelType
    additional_properties: bool
    properties: APBatchModelProperties

    def __init__(self, title: str, type: APBatchModelType, additional_properties: bool, properties: APBatchModelProperties) -> None:
        self.title = title
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class Payment:
    type: ApRouteIDType
    max_length: int
    min_length: int
    nullable: bool

    def __init__(self, type: ApRouteIDType, max_length: int, min_length: int, nullable: bool) -> None:
        self.type = type
        self.max_length = max_length
        self.min_length = min_length
        self.nullable = nullable


class FontSizeClass:
    nullable: bool
    ref: str

    def __init__(self, nullable: bool, ref: str) -> None:
        self.nullable = nullable
        self.ref = ref


class APBatchPaymentModelProperties:
    payment_status: FontSizeClass
    payment_comments: Payment

    def __init__(self, payment_status: FontSizeClass, payment_comments: Payment) -> None:
        self.payment_status = payment_status
        self.payment_comments = payment_comments


class APBatchPaymentModel:
    type: APBatchModelType
    additional_properties: bool
    properties: APBatchPaymentModelProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: APBatchPaymentModelProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class APBatchRunModelProperties:
    id: PaymentComments
    batch_id: PaymentComments
    ap_route_id: InvoiceCountClass
    sent_to_ap_date_time: InvoiceCountClass
    run_date_time: InvoiceCountClass
    invoice_count: InvoiceCountClass

    def __init__(self, id: PaymentComments, batch_id: PaymentComments, ap_route_id: InvoiceCountClass, sent_to_ap_date_time: InvoiceCountClass, run_date_time: InvoiceCountClass, invoice_count: InvoiceCountClass) -> None:
        self.id = id
        self.batch_id = batch_id
        self.ap_route_id = ap_route_id
        self.sent_to_ap_date_time = sent_to_ap_date_time
        self.run_date_time = run_date_time
        self.invoice_count = invoice_count


class ApBatchRunModel:
    title: str
    type: APBatchModelType
    additional_properties: bool
    properties: APBatchRunModelProperties

    def __init__(self, title: str, type: APBatchModelType, additional_properties: bool, properties: APBatchRunModelProperties) -> None:
        self.title = title
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class APDataExchangeFileModelProperties:
    download_link: PaymentComments
    file_name: PaymentComments
    file_size_in_bytes: InvoiceCountClass
    md5_hash: PaymentComments

    def __init__(self, download_link: PaymentComments, file_name: PaymentComments, file_size_in_bytes: InvoiceCountClass, md5_hash: PaymentComments) -> None:
        self.download_link = download_link
        self.file_name = file_name
        self.file_size_in_bytes = file_size_in_bytes
        self.md5_hash = md5_hash


class APDataExchangeFileModel:
    type: APBatchModelType
    additional_properties: bool
    properties: APDataExchangeFileModelProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: APDataExchangeFileModelProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class APDataExchangeFileRequestProperties:
    file_type: FileFormatClass
    file_format: FileFormatClass
    include_supporting_documents: IncludeSupportingDocumentsClass
    orientation: FontSizeClass
    font_size: FontSizeClass

    def __init__(self, file_type: FileFormatClass, file_format: FileFormatClass, include_supporting_documents: IncludeSupportingDocumentsClass, orientation: FontSizeClass, font_size: FontSizeClass) -> None:
        self.file_type = file_type
        self.file_format = file_format
        self.include_supporting_documents = include_supporting_documents
        self.orientation = orientation
        self.font_size = font_size


class APDataExchangeFileRequest:
    type: APBatchModelType
    additional_properties: bool
    required: List[str]
    properties: APDataExchangeFileRequestProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, required: List[str], properties: APDataExchangeFileRequestProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.required = required
        self.properties = properties


class ApDataFileFormat:
    type: ApRouteIDType
    description: str
    x_enum_names: List[str]
    enum: List[str]
    x_enum_flags: Optional[bool]

    def __init__(self, type: ApRouteIDType, description: str, x_enum_names: List[str], enum: List[str], x_enum_flags: Optional[bool]) -> None:
        self.type = type
        self.description = description
        self.x_enum_names = x_enum_names
        self.enum = enum
        self.x_enum_flags = x_enum_flags


class APRouteEmailModelProperties:
    enabled: IncludeSupportingDocumentsClass

    def __init__(self, enabled: IncludeSupportingDocumentsClass) -> None:
        self.enabled = enabled


class ApRouteModel:
    type: APBatchModelType
    additional_properties: bool
    properties: APRouteEmailModelProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: APRouteEmailModelProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class APRouteModelProperties:
    id: InvoiceCountClass
    name: PaymentComments
    active: IncludeSupportingDocumentsClass
    emails: FontSizeClass
    sftp: FontSizeClass
    web_service: FontSizeClass

    def __init__(self, id: InvoiceCountClass, name: PaymentComments, active: IncludeSupportingDocumentsClass, emails: FontSizeClass, sftp: FontSizeClass, web_service: FontSizeClass) -> None:
        self.id = id
        self.name = name
        self.active = active
        self.emails = emails
        self.sftp = sftp
        self.web_service = web_service


class APRouteModelClass:
    title: str
    type: APBatchModelType
    additional_properties: bool
    properties: APRouteModelProperties

    def __init__(self, title: str, type: APBatchModelType, additional_properties: bool, properties: APRouteModelProperties) -> None:
        self.title = title
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class AccountID:
    type: ApRouteIDType
    format: Optional[str]
    nullable: Optional[bool]

    def __init__(self, type: ApRouteIDType, format: Optional[str], nullable: Optional[bool]) -> None:
        self.type = type
        self.format = format
        self.nullable = nullable


class APRouteWebServiceModelProperties:
    email_notification_enabled: PaymentComments
    account_id: AccountID

    def __init__(self, email_notification_enabled: PaymentComments, account_id: AccountID) -> None:
        self.email_notification_enabled = email_notification_enabled
        self.account_id = account_id


class APRouteWebServiceModel:
    type: APBatchModelType
    additional_properties: bool
    properties: APRouteWebServiceModelProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: APRouteWebServiceModelProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class Apply:
    description: str
    nullable: Optional[bool]
    ref: Optional[str]
    type: Optional[ApRouteIDType]

    def __init__(self, description: str, nullable: Optional[bool], ref: Optional[str], type: Optional[ApRouteIDType]) -> None:
        self.description = description
        self.nullable = nullable
        self.ref = ref
        self.type = type


class AdditionalProperties:
    pass

    def __init__(self, ) -> None:
        pass


class ConcurrencyPropertiesClass:
    type: APBatchModelType
    nullable: bool
    additional_properties: AdditionalProperties

    def __init__(self, type: APBatchModelType, nullable: bool, additional_properties: AdditionalProperties) -> None:
        self.type = type
        self.nullable = nullable
        self.additional_properties = additional_properties


class Context:
    description: str
    nullable: bool
    ref: str

    def __init__(self, description: str, nullable: bool, ref: str) -> None:
        self.description = description
        self.nullable = nullable
        self.ref = ref


class NoCacheHeadersItems:
    type: Optional[ApRouteIDType]
    ref: Optional[str]

    def __init__(self, type: Optional[ApRouteIDType], ref: Optional[str]) -> None:
        self.type = type
        self.ref = ref


class NoCacheHeaders:
    type: ApRouteIDType
    nullable: bool
    items: Optional[NoCacheHeadersItems]
    description: Optional[str]

    def __init__(self, type: ApRouteIDType, nullable: bool, items: Optional[NoCacheHeadersItems], description: Optional[str]) -> None:
        self.type = type
        self.nullable = nullable
        self.items = items
        self.description = description


class IsAny:
    type: APBatchModelType
    description: str

    def __init__(self, type: APBatchModelType, description: str) -> None:
        self.type = type
        self.description = description


class Extensions:
    type: ApRouteIDType
    description: Optional[str]
    nullable: Optional[bool]
    items: Optional[FileFormatClass]
    format: Optional[str]
    example: Optional[str]

    def __init__(self, type: ApRouteIDType, description: Optional[str], nullable: Optional[bool], items: Optional[FileFormatClass], format: Optional[str], example: Optional[str]) -> None:
        self.type = type
        self.description = description
        self.nullable = nullable
        self.items = items
        self.format = format
        self.example = example


class Item:
    nullable: bool

    def __init__(self, nullable: bool) -> None:
        self.nullable = nullable


class RawValue:
    type: ApRouteIDType
    description: str
    nullable: bool

    def __init__(self, type: ApRouteIDType, description: str, nullable: bool) -> None:
        self.type = type
        self.description = description
        self.nullable = nullable


class ApplyClauseProperties:
    transformations: Optional[Extensions]
    enable_expand: Optional[IsAny]
    enable_select: Optional[IsAny]
    enable_count: Optional[IsAny]
    enable_order_by: Optional[IsAny]
    enable_filter: Optional[IsAny]
    max_top: Optional[Extensions]
    enable_skip_token: Optional[IsAny]
    item: Optional[Item]
    is_well_formed: Optional[IsAny]
    entity_type: Optional[Extensions]
    is_any: Optional[IsAny]
    is_if_none_match: Optional[IsAny]
    concurrency_properties: Optional[ConcurrencyPropertiesClass]
    dependent_property: Optional[Context]
    principal_property: Optional[Context]
    expression: Optional[Context]
    range_variable: Optional[Context]
    item_type: Optional[Context]
    context: Optional[Context]
    validator: Optional[Context]
    filter_clause: Optional[Context]
    raw_value: Optional[RawValue]
    edm_type: Optional[Context]
    navigation_source: Optional[Context]
    segments: Optional[Extensions]
    path_template: Optional[Extensions]
    path: Optional[Extensions]
    request: Optional[Context]
    raw_values: Optional[Context]
    select_expand: Optional[Context]
    apply: Optional[Apply]
    filter: Optional[Apply]
    order_by: Optional[Apply]
    skip: Optional[Apply]
    skip_token: Optional[Apply]
    top: Optional[Apply]
    count: Optional[Apply]
    if_match: Optional[Context]
    if_none_match: Optional[Context]
    select: Optional[NoCacheHeaders]
    expand: Optional[NoCacheHeaders]
    format: Optional[NoCacheHeaders]
    delta_token: Optional[NoCacheHeaders]
    order_by_nodes: Optional[Extensions]
    order_by_clause: Optional[Context]
    raw_select: Optional[Extensions]
    raw_expand: Optional[Extensions]
    select_expand_clause: Optional[Context]
    levels_max_literal_expansion_depth: Optional[Extensions]
    value: Optional[Extensions]

    def __init__(self, transformations: Optional[Extensions], enable_expand: Optional[IsAny], enable_select: Optional[IsAny], enable_count: Optional[IsAny], enable_order_by: Optional[IsAny], enable_filter: Optional[IsAny], max_top: Optional[Extensions], enable_skip_token: Optional[IsAny], item: Optional[Item], is_well_formed: Optional[IsAny], entity_type: Optional[Extensions], is_any: Optional[IsAny], is_if_none_match: Optional[IsAny], concurrency_properties: Optional[ConcurrencyPropertiesClass], dependent_property: Optional[Context], principal_property: Optional[Context], expression: Optional[Context], range_variable: Optional[Context], item_type: Optional[Context], context: Optional[Context], validator: Optional[Context], filter_clause: Optional[Context], raw_value: Optional[RawValue], edm_type: Optional[Context], navigation_source: Optional[Context], segments: Optional[Extensions], path_template: Optional[Extensions], path: Optional[Extensions], request: Optional[Context], raw_values: Optional[Context], select_expand: Optional[Context], apply: Optional[Apply], filter: Optional[Apply], order_by: Optional[Apply], skip: Optional[Apply], skip_token: Optional[Apply], top: Optional[Apply], count: Optional[Apply], if_match: Optional[Context], if_none_match: Optional[Context], select: Optional[NoCacheHeaders], expand: Optional[NoCacheHeaders], format: Optional[NoCacheHeaders], delta_token: Optional[NoCacheHeaders], order_by_nodes: Optional[Extensions], order_by_clause: Optional[Context], raw_select: Optional[Extensions], raw_expand: Optional[Extensions], select_expand_clause: Optional[Context], levels_max_literal_expansion_depth: Optional[Extensions], value: Optional[Extensions]) -> None:
        self.transformations = transformations
        self.enable_expand = enable_expand
        self.enable_select = enable_select
        self.enable_count = enable_count
        self.enable_order_by = enable_order_by
        self.enable_filter = enable_filter
        self.max_top = max_top
        self.enable_skip_token = enable_skip_token
        self.item = item
        self.is_well_formed = is_well_formed
        self.entity_type = entity_type
        self.is_any = is_any
        self.is_if_none_match = is_if_none_match
        self.concurrency_properties = concurrency_properties
        self.dependent_property = dependent_property
        self.principal_property = principal_property
        self.expression = expression
        self.range_variable = range_variable
        self.item_type = item_type
        self.context = context
        self.validator = validator
        self.filter_clause = filter_clause
        self.raw_value = raw_value
        self.edm_type = edm_type
        self.navigation_source = navigation_source
        self.segments = segments
        self.path_template = path_template
        self.path = path
        self.request = request
        self.raw_values = raw_values
        self.select_expand = select_expand
        self.apply = apply
        self.filter = filter
        self.order_by = order_by
        self.skip = skip
        self.skip_token = skip_token
        self.top = top
        self.count = count
        self.if_match = if_match
        self.if_none_match = if_none_match
        self.select = select
        self.expand = expand
        self.format = format
        self.delta_token = delta_token
        self.order_by_nodes = order_by_nodes
        self.order_by_clause = order_by_clause
        self.raw_select = raw_select
        self.raw_expand = raw_expand
        self.select_expand_clause = select_expand_clause
        self.levels_max_literal_expansion_depth = levels_max_literal_expansion_depth
        self.value = value


class ApplyClause:
    type: APBatchModelType
    description: str
    additional_properties: bool
    properties: Optional[ApplyClauseProperties]

    def __init__(self, type: APBatchModelType, description: str, additional_properties: bool, properties: Optional[ApplyClauseProperties]) -> None:
        self.type = type
        self.description = description
        self.additional_properties = additional_properties
        self.properties = properties


class ContainerElementKind:
    description: str
    ref: str

    def __init__(self, description: str, ref: str) -> None:
        self.description = description
        self.ref = ref


class ApplyQueryOptionProperties:
    context: Optional[Context]
    result_clr_type: Optional[Extensions]
    apply_clause: Optional[Context]
    raw_value: Optional[Extensions]
    elements: Optional[Extensions]
    container_element_kind: Optional[ContainerElementKind]
    container: Optional[Context]
    expression_kind: Optional[ContainerElementKind]
    schema_elements: Optional[Extensions]
    vocabulary_annotations: Optional[Extensions]
    referenced_models: Optional[Extensions]
    declared_namespaces: Optional[NoCacheHeaders]
    direct_value_annotations_manager: Optional[Context]
    entity_container: Optional[Context]
    partner: Optional[Context]
    on_delete: Optional[ContainerElementKind]
    contains_target: Optional[IsAny]
    referential_constraint: Optional[Context]
    navigation_property: Optional[Context]
    target: Optional[Context]
    path: Optional[Apply]
    navigation_property_bindings: Optional[Extensions]
    type: Optional[Context]
    path_segments: Optional[NoCacheHeaders]
    property_pairs: Optional[NoCacheHeaders]
    schema_element_kind: Optional[ContainerElementKind]
    namespace: Optional[Extensions]
    default_value_string: Optional[Extensions]
    applies_to: Optional[NoCacheHeaders]
    default_value: Optional[NoCacheHeaders]
    type_kind: Optional[ContainerElementKind]
    is_nullable: Optional[IsAny]
    definition: Optional[Context]
    identifier: Optional[Extensions]
    request: Optional[Context]
    raw_values: Optional[Context]
    select_expand: Optional[Context]
    apply: Optional[Context]
    filter: Optional[Context]
    order_by: Optional[Context]
    skip: Optional[Context]
    skip_token: Optional[Context]
    top: Optional[Context]
    count: Optional[Context]
    validator: Optional[Context]
    if_match: Optional[FontSizeClass]
    if_none_match: Optional[FontSizeClass]
    then_by: Optional[Context]
    expression: Optional[Context]
    direction: Optional[ContainerElementKind]
    range_variable: Optional[Context]
    item_type: Optional[Context]
    kind: Optional[ContainerElementKind]

    def __init__(self, context: Optional[Context], result_clr_type: Optional[Extensions], apply_clause: Optional[Context], raw_value: Optional[Extensions], elements: Optional[Extensions], container_element_kind: Optional[ContainerElementKind], container: Optional[Context], expression_kind: Optional[ContainerElementKind], schema_elements: Optional[Extensions], vocabulary_annotations: Optional[Extensions], referenced_models: Optional[Extensions], declared_namespaces: Optional[NoCacheHeaders], direct_value_annotations_manager: Optional[Context], entity_container: Optional[Context], partner: Optional[Context], on_delete: Optional[ContainerElementKind], contains_target: Optional[IsAny], referential_constraint: Optional[Context], navigation_property: Optional[Context], target: Optional[Context], path: Optional[Apply], navigation_property_bindings: Optional[Extensions], type: Optional[Context], path_segments: Optional[NoCacheHeaders], property_pairs: Optional[NoCacheHeaders], schema_element_kind: Optional[ContainerElementKind], namespace: Optional[Extensions], default_value_string: Optional[Extensions], applies_to: Optional[NoCacheHeaders], default_value: Optional[NoCacheHeaders], type_kind: Optional[ContainerElementKind], is_nullable: Optional[IsAny], definition: Optional[Context], identifier: Optional[Extensions], request: Optional[Context], raw_values: Optional[Context], select_expand: Optional[Context], apply: Optional[Context], filter: Optional[Context], order_by: Optional[Context], skip: Optional[Context], skip_token: Optional[Context], top: Optional[Context], count: Optional[Context], validator: Optional[Context], if_match: Optional[FontSizeClass], if_none_match: Optional[FontSizeClass], then_by: Optional[Context], expression: Optional[Context], direction: Optional[ContainerElementKind], range_variable: Optional[Context], item_type: Optional[Context], kind: Optional[ContainerElementKind]) -> None:
        self.context = context
        self.result_clr_type = result_clr_type
        self.apply_clause = apply_clause
        self.raw_value = raw_value
        self.elements = elements
        self.container_element_kind = container_element_kind
        self.container = container
        self.expression_kind = expression_kind
        self.schema_elements = schema_elements
        self.vocabulary_annotations = vocabulary_annotations
        self.referenced_models = referenced_models
        self.declared_namespaces = declared_namespaces
        self.direct_value_annotations_manager = direct_value_annotations_manager
        self.entity_container = entity_container
        self.partner = partner
        self.on_delete = on_delete
        self.contains_target = contains_target
        self.referential_constraint = referential_constraint
        self.navigation_property = navigation_property
        self.target = target
        self.path = path
        self.navigation_property_bindings = navigation_property_bindings
        self.type = type
        self.path_segments = path_segments
        self.property_pairs = property_pairs
        self.schema_element_kind = schema_element_kind
        self.namespace = namespace
        self.default_value_string = default_value_string
        self.applies_to = applies_to
        self.default_value = default_value
        self.type_kind = type_kind
        self.is_nullable = is_nullable
        self.definition = definition
        self.identifier = identifier
        self.request = request
        self.raw_values = raw_values
        self.select_expand = select_expand
        self.apply = apply
        self.filter = filter
        self.order_by = order_by
        self.skip = skip
        self.skip_token = skip_token
        self.top = top
        self.count = count
        self.validator = validator
        self.if_match = if_match
        self.if_none_match = if_none_match
        self.then_by = then_by
        self.expression = expression
        self.direction = direction
        self.range_variable = range_variable
        self.item_type = item_type
        self.kind = kind


class ApplyQueryOption:
    type: APBatchModelType
    description: str
    additional_properties: bool
    properties: Optional[ApplyQueryOptionProperties]
    x_abstract: Optional[bool]

    def __init__(self, type: APBatchModelType, description: str, additional_properties: bool, properties: Optional[ApplyQueryOptionProperties], x_abstract: Optional[bool]) -> None:
        self.type = type
        self.description = description
        self.additional_properties = additional_properties
        self.properties = properties
        self.x_abstract = x_abstract


class AuthenticationHeaderValueProperties:
    scheme: PaymentComments
    parameter: PaymentComments

    def __init__(self, scheme: PaymentComments, parameter: PaymentComments) -> None:
        self.scheme = scheme
        self.parameter = parameter


class AuthenticationHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: AuthenticationHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: AuthenticationHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class CacheControlHeaderValueProperties:
    no_cache: IncludeSupportingDocumentsClass
    no_cache_headers: NoCacheHeaders
    no_store: IncludeSupportingDocumentsClass
    max_age: AccountID
    shared_max_age: AccountID
    max_stale: IncludeSupportingDocumentsClass
    max_stale_limit: AccountID
    min_fresh: AccountID
    no_transform: IncludeSupportingDocumentsClass
    only_if_cached: IncludeSupportingDocumentsClass
    public: IncludeSupportingDocumentsClass
    private: IncludeSupportingDocumentsClass
    private_headers: NoCacheHeaders
    must_revalidate: IncludeSupportingDocumentsClass
    proxy_revalidate: IncludeSupportingDocumentsClass
    extensions: Extensions

    def __init__(self, no_cache: IncludeSupportingDocumentsClass, no_cache_headers: NoCacheHeaders, no_store: IncludeSupportingDocumentsClass, max_age: AccountID, shared_max_age: AccountID, max_stale: IncludeSupportingDocumentsClass, max_stale_limit: AccountID, min_fresh: AccountID, no_transform: IncludeSupportingDocumentsClass, only_if_cached: IncludeSupportingDocumentsClass, public: IncludeSupportingDocumentsClass, private: IncludeSupportingDocumentsClass, private_headers: NoCacheHeaders, must_revalidate: IncludeSupportingDocumentsClass, proxy_revalidate: IncludeSupportingDocumentsClass, extensions: Extensions) -> None:
        self.no_cache = no_cache
        self.no_cache_headers = no_cache_headers
        self.no_store = no_store
        self.max_age = max_age
        self.shared_max_age = shared_max_age
        self.max_stale = max_stale
        self.max_stale_limit = max_stale_limit
        self.min_fresh = min_fresh
        self.no_transform = no_transform
        self.only_if_cached = only_if_cached
        self.public = public
        self.private = private
        self.private_headers = private_headers
        self.must_revalidate = must_revalidate
        self.proxy_revalidate = proxy_revalidate
        self.extensions = extensions


class CacheControlHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: CacheControlHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: CacheControlHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class ContentDispositionHeaderValueProperties:
    disposition_type: PaymentComments
    parameters: Extensions
    name: PaymentComments
    file_name: PaymentComments
    file_name_star: PaymentComments
    creation_date: AccountID
    modification_date: AccountID
    read_date: AccountID
    size: AccountID

    def __init__(self, disposition_type: PaymentComments, parameters: Extensions, name: PaymentComments, file_name: PaymentComments, file_name_star: PaymentComments, creation_date: AccountID, modification_date: AccountID, read_date: AccountID, size: AccountID) -> None:
        self.disposition_type = disposition_type
        self.parameters = parameters
        self.name = name
        self.file_name = file_name
        self.file_name_star = file_name_star
        self.creation_date = creation_date
        self.modification_date = modification_date
        self.read_date = read_date
        self.size = size


class ContentDispositionHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: ContentDispositionHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: ContentDispositionHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class ContentRangeHeaderValueProperties:
    unit: PaymentComments
    properties_from: AccountID
    to: AccountID
    length: AccountID
    has_length: IncludeSupportingDocumentsClass
    has_range: IncludeSupportingDocumentsClass

    def __init__(self, unit: PaymentComments, properties_from: AccountID, to: AccountID, length: AccountID, has_length: IncludeSupportingDocumentsClass, has_range: IncludeSupportingDocumentsClass) -> None:
        self.unit = unit
        self.properties_from = properties_from
        self.to = to
        self.length = length
        self.has_length = has_length
        self.has_range = has_range


class ContentRangeHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: ContentRangeHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: ContentRangeHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class CountQueryOptionProperties:
    context: Optional[Context]
    raw_value: Optional[Extensions]
    value: Optional[Apply]
    validator: Optional[Context]
    qualifier: Optional[NoCacheHeaders]
    term: Optional[Context]
    target: Optional[Context]
    default_query_settings: Optional[Context]
    model: Optional[Context]
    element_type: Optional[Context]
    navigation_source: Optional[Context]
    element_clr_type: Optional[Extensions]
    path: Optional[Context]
    request_container: Optional[Context]
    request: Optional[Context]
    raw_values: Optional[Context]
    select_expand: Optional[Context]
    apply: Optional[Context]
    filter: Optional[Context]
    order_by: Optional[Context]
    skip: Optional[Context]
    skip_token: Optional[Context]
    top: Optional[Context]
    count: Optional[Context]
    if_match: Optional[FontSizeClass]
    if_none_match: Optional[FontSizeClass]
    ensure_stable_ordering: Optional[IsAny]
    handle_null_propagation: Optional[ContainerElementKind]
    enable_constant_parameterization: Optional[IsAny]
    enable_correlated_subquery_buffering: Optional[IsAny]
    page_size: Optional[Extensions]
    handle_reference_navigation_property_expand_filter: Optional[IsAny]
    direction: Optional[ContainerElementKind]
    selected_items: Optional[Extensions]
    all_selected: Optional[IsAny]

    def __init__(self, context: Optional[Context], raw_value: Optional[Extensions], value: Optional[Apply], validator: Optional[Context], qualifier: Optional[NoCacheHeaders], term: Optional[Context], target: Optional[Context], default_query_settings: Optional[Context], model: Optional[Context], element_type: Optional[Context], navigation_source: Optional[Context], element_clr_type: Optional[Extensions], path: Optional[Context], request_container: Optional[Context], request: Optional[Context], raw_values: Optional[Context], select_expand: Optional[Context], apply: Optional[Context], filter: Optional[Context], order_by: Optional[Context], skip: Optional[Context], skip_token: Optional[Context], top: Optional[Context], count: Optional[Context], if_match: Optional[FontSizeClass], if_none_match: Optional[FontSizeClass], ensure_stable_ordering: Optional[IsAny], handle_null_propagation: Optional[ContainerElementKind], enable_constant_parameterization: Optional[IsAny], enable_correlated_subquery_buffering: Optional[IsAny], page_size: Optional[Extensions], handle_reference_navigation_property_expand_filter: Optional[IsAny], direction: Optional[ContainerElementKind], selected_items: Optional[Extensions], all_selected: Optional[IsAny]) -> None:
        self.context = context
        self.raw_value = raw_value
        self.value = value
        self.validator = validator
        self.qualifier = qualifier
        self.term = term
        self.target = target
        self.default_query_settings = default_query_settings
        self.model = model
        self.element_type = element_type
        self.navigation_source = navigation_source
        self.element_clr_type = element_clr_type
        self.path = path
        self.request_container = request_container
        self.request = request
        self.raw_values = raw_values
        self.select_expand = select_expand
        self.apply = apply
        self.filter = filter
        self.order_by = order_by
        self.skip = skip
        self.skip_token = skip_token
        self.top = top
        self.count = count
        self.if_match = if_match
        self.if_none_match = if_none_match
        self.ensure_stable_ordering = ensure_stable_ordering
        self.handle_null_propagation = handle_null_propagation
        self.enable_constant_parameterization = enable_constant_parameterization
        self.enable_correlated_subquery_buffering = enable_correlated_subquery_buffering
        self.page_size = page_size
        self.handle_reference_navigation_property_expand_filter = handle_reference_navigation_property_expand_filter
        self.direction = direction
        self.selected_items = selected_items
        self.all_selected = all_selected


class CountQueryOption:
    type: APBatchModelType
    description: str
    additional_properties: bool
    properties: Optional[CountQueryOptionProperties]
    x_abstract: Optional[bool]

    def __init__(self, type: APBatchModelType, description: str, additional_properties: bool, properties: Optional[CountQueryOptionProperties], x_abstract: Optional[bool]) -> None:
        self.type = type
        self.description = description
        self.additional_properties = additional_properties
        self.properties = properties
        self.x_abstract = x_abstract


class EdmContainerElementKind:
    type: ApRouteIDType
    description: str
    x_enum_names: List[str]
    enum: List[int]

    def __init__(self, type: ApRouteIDType, description: str, x_enum_names: List[str], enum: List[int]) -> None:
        self.type = type
        self.description = description
        self.x_enum_names = x_enum_names
        self.enum = enum


class EntityTagHeaderValueProperties:
    tag: PaymentComments
    is_weak: IncludeSupportingDocumentsClass

    def __init__(self, tag: PaymentComments, is_weak: IncludeSupportingDocumentsClass) -> None:
        self.tag = tag
        self.is_weak = is_weak


class EntityTagHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: EntityTagHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: EntityTagHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class PurpleProperties:
    code: IncludeSupportingDocumentsClass
    message: IncludeSupportingDocumentsClass
    target: IncludeSupportingDocumentsClass

    def __init__(self, code: IncludeSupportingDocumentsClass, message: IncludeSupportingDocumentsClass, target: IncludeSupportingDocumentsClass) -> None:
        self.code = code
        self.message = message
        self.target = target


class DetailsItems:
    type: APBatchModelType
    required: List[str]
    properties: PurpleProperties

    def __init__(self, type: APBatchModelType, required: List[str], properties: PurpleProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties


class Details:
    type: ApRouteIDType
    items: DetailsItems

    def __init__(self, type: ApRouteIDType, items: DetailsItems) -> None:
        self.type = type
        self.items = items


class ErrorProperties:
    code: IncludeSupportingDocumentsClass
    message: IncludeSupportingDocumentsClass
    target: IncludeSupportingDocumentsClass
    details: Details
    innererror: IsAny

    def __init__(self, code: IncludeSupportingDocumentsClass, message: IncludeSupportingDocumentsClass, target: IncludeSupportingDocumentsClass, details: Details, innererror: IsAny) -> None:
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror


class PropertiesError:
    type: APBatchModelType
    required: List[str]
    properties: ErrorProperties

    def __init__(self, type: APBatchModelType, required: List[str], properties: ErrorProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties


class ErrorResponseProperties:
    error: PropertiesError

    def __init__(self, error: PropertiesError) -> None:
        self.error = error


class ErrorResponse:
    type: APBatchModelType
    required: List[str]
    properties: ErrorResponseProperties

    def __init__(self, type: APBatchModelType, required: List[str], properties: ErrorResponseProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties


class HTTPContentProperties:
    headers: Optional[FontSizeClass]
    context: Optional[Context]
    raw_value: Optional[Extensions]
    value: Optional[Extensions]
    validator: Optional[Context]
    query_settings: Optional[Context]
    query_options: Optional[Context]

    def __init__(self, headers: Optional[FontSizeClass], context: Optional[Context], raw_value: Optional[Extensions], value: Optional[Extensions], validator: Optional[Context], query_settings: Optional[Context], query_options: Optional[Context]) -> None:
        self.headers = headers
        self.context = context
        self.raw_value = raw_value
        self.value = value
        self.validator = validator
        self.query_settings = query_settings
        self.query_options = query_options


class HTTPContent:
    type: APBatchModelType
    x_abstract: Optional[bool]
    additional_properties: bool
    properties: Optional[HTTPContentProperties]
    description: Optional[str]

    def __init__(self, type: APBatchModelType, x_abstract: Optional[bool], additional_properties: bool, properties: Optional[HTTPContentProperties], description: Optional[str]) -> None:
        self.type = type
        self.x_abstract = x_abstract
        self.additional_properties = additional_properties
        self.properties = properties
        self.description = description


class HTTPContentHeadersProperties:
    allow: NoCacheHeaders
    content_disposition: FontSizeClass
    content_encoding: NoCacheHeaders
    content_language: NoCacheHeaders
    content_length: AccountID
    content_location: AccountID
    content_md5: AccountID
    content_range: FontSizeClass
    content_type: FontSizeClass
    expires: Extensions
    last_modified: Extensions

    def __init__(self, allow: NoCacheHeaders, content_disposition: FontSizeClass, content_encoding: NoCacheHeaders, content_language: NoCacheHeaders, content_length: AccountID, content_location: AccountID, content_md5: AccountID, content_range: FontSizeClass, content_type: FontSizeClass, expires: Extensions, last_modified: Extensions) -> None:
        self.allow = allow
        self.content_disposition = content_disposition
        self.content_encoding = content_encoding
        self.content_language = content_language
        self.content_length = content_length
        self.content_location = content_location
        self.content_md5 = content_md5
        self.content_range = content_range
        self.content_type = content_type
        self.expires = expires
        self.last_modified = last_modified


class HTTPContentHeaders:
    type: APBatchModelType
    additional_properties: bool
    properties: HTTPContentHeadersProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: HTTPContentHeadersProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class HTTPMethodProperties:
    method: PaymentComments

    def __init__(self, method: PaymentComments) -> None:
        self.method = method


class HTTPMethod:
    type: APBatchModelType
    additional_properties: bool
    properties: HTTPMethodProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: HTTPMethodProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class HTTPRequestHeadersProperties:
    accept: Extensions
    accept_charset: Extensions
    accept_encoding: Extensions
    accept_language: Extensions
    authorization: FontSizeClass
    expect: Extensions
    expect_continue: PaymentComments
    properties_from: PaymentComments
    host: PaymentComments
    if_match: Extensions
    if_modified_since: Extensions
    if_none_match: Extensions
    if_range: FontSizeClass
    if_unmodified_since: Extensions
    max_forwards: Extensions
    proxy_authorization: FontSizeClass
    range: FontSizeClass
    referrer: AccountID
    te: Extensions
    user_agent: Extensions
    cache_control: FontSizeClass
    connection: NoCacheHeaders
    connection_close: PaymentComments
    date: Extensions
    pragma: Extensions
    trailer: NoCacheHeaders
    transfer_encoding: Extensions
    transfer_encoding_chunked: PaymentComments
    upgrade: Extensions
    via: Extensions
    warning: Extensions

    def __init__(self, accept: Extensions, accept_charset: Extensions, accept_encoding: Extensions, accept_language: Extensions, authorization: FontSizeClass, expect: Extensions, expect_continue: PaymentComments, properties_from: PaymentComments, host: PaymentComments, if_match: Extensions, if_modified_since: Extensions, if_none_match: Extensions, if_range: FontSizeClass, if_unmodified_since: Extensions, max_forwards: Extensions, proxy_authorization: FontSizeClass, range: FontSizeClass, referrer: AccountID, te: Extensions, user_agent: Extensions, cache_control: FontSizeClass, connection: NoCacheHeaders, connection_close: PaymentComments, date: Extensions, pragma: Extensions, trailer: NoCacheHeaders, transfer_encoding: Extensions, transfer_encoding_chunked: PaymentComments, upgrade: Extensions, via: Extensions, warning: Extensions) -> None:
        self.accept = accept
        self.accept_charset = accept_charset
        self.accept_encoding = accept_encoding
        self.accept_language = accept_language
        self.authorization = authorization
        self.expect = expect
        self.expect_continue = expect_continue
        self.properties_from = properties_from
        self.host = host
        self.if_match = if_match
        self.if_modified_since = if_modified_since
        self.if_none_match = if_none_match
        self.if_range = if_range
        self.if_unmodified_since = if_unmodified_since
        self.max_forwards = max_forwards
        self.proxy_authorization = proxy_authorization
        self.range = range
        self.referrer = referrer
        self.te = te
        self.user_agent = user_agent
        self.cache_control = cache_control
        self.connection = connection
        self.connection_close = connection_close
        self.date = date
        self.pragma = pragma
        self.trailer = trailer
        self.transfer_encoding = transfer_encoding
        self.transfer_encoding_chunked = transfer_encoding_chunked
        self.upgrade = upgrade
        self.via = via
        self.warning = warning


class HTTPRequestHeaders:
    type: APBatchModelType
    additional_properties: bool
    properties: HTTPRequestHeadersProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: HTTPRequestHeadersProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class HTTPRequestMessageProperties:
    version: FontSizeClass
    content: FontSizeClass
    method: FontSizeClass
    request_uri: Extensions
    headers: FontSizeClass
    properties: ConcurrencyPropertiesClass

    def __init__(self, version: FontSizeClass, content: FontSizeClass, method: FontSizeClass, request_uri: Extensions, headers: FontSizeClass, properties: ConcurrencyPropertiesClass) -> None:
        self.version = version
        self.content = content
        self.method = method
        self.request_uri = request_uri
        self.headers = headers
        self.properties = properties


class HTTPRequestMessage:
    type: APBatchModelType
    additional_properties: bool
    properties: HTTPRequestMessageProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: HTTPRequestMessageProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class ApRouteTrackerIDClass:
    type: ApRouteIDType
    read_only: bool
    format: Format

    def __init__(self, type: ApRouteIDType, read_only: bool, format: Format) -> None:
        self.type = type
        self.read_only = read_only
        self.format = format


class NumberClass:
    type: ApRouteIDType
    read_only: bool
    nullable: bool

    def __init__(self, type: ApRouteIDType, read_only: bool, nullable: bool) -> None:
        self.type = type
        self.read_only = read_only
        self.nullable = nullable


class InvoicePaymentModelProperties:
    id: ApRouteTrackerIDClass
    number: NumberClass
    invoice_date_time: ApRouteTrackerIDClass
    matter_id: ApRouteTrackerIDClass
    vendor_id: ApRouteTrackerIDClass
    vendor_name: NumberClass
    vendor_short_name: NumberClass
    ap_route_id: ApRouteTrackerIDClass
    ap_route_tracker_id: ApRouteTrackerIDClass
    sent_to_ap_date_time: ApRouteTrackerIDClass
    batch_id: NumberClass
    batch_run_date_time: ApRouteTrackerIDClass
    approved_total: ApRouteTrackerIDClass
    approved_date_time: ApRouteTrackerIDClass
    payment_number: PaymentComments
    payment_status: PaymentComments
    payment_comments: PaymentComments
    payment_date_time: AccountID
    exchange_rate: AccountID
    payment_amount: AccountID

    def __init__(self, id: ApRouteTrackerIDClass, number: NumberClass, invoice_date_time: ApRouteTrackerIDClass, matter_id: ApRouteTrackerIDClass, vendor_id: ApRouteTrackerIDClass, vendor_name: NumberClass, vendor_short_name: NumberClass, ap_route_id: ApRouteTrackerIDClass, ap_route_tracker_id: ApRouteTrackerIDClass, sent_to_ap_date_time: ApRouteTrackerIDClass, batch_id: NumberClass, batch_run_date_time: ApRouteTrackerIDClass, approved_total: ApRouteTrackerIDClass, approved_date_time: ApRouteTrackerIDClass, payment_number: PaymentComments, payment_status: PaymentComments, payment_comments: PaymentComments, payment_date_time: AccountID, exchange_rate: AccountID, payment_amount: AccountID) -> None:
        self.id = id
        self.number = number
        self.invoice_date_time = invoice_date_time
        self.matter_id = matter_id
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
        self.vendor_short_name = vendor_short_name
        self.ap_route_id = ap_route_id
        self.ap_route_tracker_id = ap_route_tracker_id
        self.sent_to_ap_date_time = sent_to_ap_date_time
        self.batch_id = batch_id
        self.batch_run_date_time = batch_run_date_time
        self.approved_total = approved_total
        self.approved_date_time = approved_date_time
        self.payment_number = payment_number
        self.payment_status = payment_status
        self.payment_comments = payment_comments
        self.payment_date_time = payment_date_time
        self.exchange_rate = exchange_rate
        self.payment_amount = payment_amount


class InvoicePaymentModel:
    title: str
    type: APBatchModelType
    additional_properties: bool
    properties: InvoicePaymentModelProperties

    def __init__(self, title: str, type: APBatchModelType, additional_properties: bool, properties: InvoicePaymentModelProperties) -> None:
        self.title = title
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class MediaTypeHeaderValueProperties:
    char_set: PaymentComments
    parameters: NoCacheHeaders
    media_type: PaymentComments
    quality: Optional[AccountID]

    def __init__(self, char_set: PaymentComments, parameters: NoCacheHeaders, media_type: PaymentComments, quality: Optional[AccountID]) -> None:
        self.char_set = char_set
        self.parameters = parameters
        self.media_type = media_type
        self.quality = quality


class MediaTypeHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: MediaTypeHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: MediaTypeHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class NameValueHeaderValueProperties:
    name: PaymentComments
    value: PaymentComments

    def __init__(self, name: PaymentComments, value: PaymentComments) -> None:
        self.name = name
        self.value = value


class NameValueHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: NameValueHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: NameValueHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class NameValueWithParametersHeaderValueProperties:
    name: PaymentComments
    value: PaymentComments
    parameters: Extensions

    def __init__(self, name: PaymentComments, value: PaymentComments, parameters: Extensions) -> None:
        self.name = name
        self.value = value
        self.parameters = parameters


class NameValueWithParametersHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: NameValueWithParametersHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: NameValueWithParametersHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class PaymentModelProperties:
    payment_number: Payment
    payment_status: Payment
    payment_comments: Payment
    payment_date_time: AccountID
    exchange_rate: AccountID
    payment_amount: AccountID

    def __init__(self, payment_number: Payment, payment_status: Payment, payment_comments: Payment, payment_date_time: AccountID, exchange_rate: AccountID, payment_amount: AccountID) -> None:
        self.payment_number = payment_number
        self.payment_status = payment_status
        self.payment_comments = payment_comments
        self.payment_date_time = payment_date_time
        self.exchange_rate = exchange_rate
        self.payment_amount = payment_amount


class PaymentModel:
    type: APBatchModelType
    additional_properties: bool
    properties: PaymentModelProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: PaymentModelProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class ProductHeaderValueProperties:
    name: PaymentComments
    version: PaymentComments

    def __init__(self, name: PaymentComments, version: PaymentComments) -> None:
        self.name = name
        self.version = version


class ProductHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: ProductHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: ProductHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class ProductInfoHeaderValueProperties:
    product: FontSizeClass
    comment: PaymentComments

    def __init__(self, product: FontSizeClass, comment: PaymentComments) -> None:
        self.product = product
        self.comment = comment


class ProductInfoHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: ProductInfoHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: ProductInfoHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class RangeConditionHeaderValueProperties:
    date: AccountID
    entity_tag: FontSizeClass

    def __init__(self, date: AccountID, entity_tag: FontSizeClass) -> None:
        self.date = date
        self.entity_tag = entity_tag


class RangeConditionHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: RangeConditionHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: RangeConditionHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class RangeHeaderValueProperties:
    unit: PaymentComments
    ranges: Extensions

    def __init__(self, unit: PaymentComments, ranges: Extensions) -> None:
        self.unit = unit
        self.ranges = ranges


class RangeHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: RangeHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: RangeHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class RangeItemHeaderValueProperties:
    properties_from: Extensions
    to: Extensions

    def __init__(self, properties_from: Extensions, to: Extensions) -> None:
        self.properties_from = properties_from
        self.to = to


class RangeItemHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: RangeItemHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: RangeItemHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class RecipientEmailModelProperties:
    email: PaymentComments
    role: FileFormatClass
    first_name: PaymentComments
    last_name: PaymentComments
    user_id: Extensions
    recipient_type: FontSizeClass

    def __init__(self, email: PaymentComments, role: FileFormatClass, first_name: PaymentComments, last_name: PaymentComments, user_id: Extensions, recipient_type: FontSizeClass) -> None:
        self.email = email
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.recipient_type = recipient_type


class RecipientEmailModel:
    type: APBatchModelType
    additional_properties: bool
    properties: RecipientEmailModelProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: RecipientEmailModelProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class StringWithQualityHeaderValueProperties:
    value: PaymentComments
    quality: Extensions

    def __init__(self, value: PaymentComments, quality: Extensions) -> None:
        self.value = value
        self.quality = quality


class StringWithQualityHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: StringWithQualityHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: StringWithQualityHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class PurpleValue:
    type: ApRouteIDType
    items: ApBatchModel

    def __init__(self, type: ApRouteIDType, items: ApBatchModel) -> None:
        self.type = type
        self.items = items


class TrackerODataResponseOfAPBatchModelProperties:
    count: IncludeSupportingDocumentsClass
    value: PurpleValue
    next_link: IncludeSupportingDocumentsClass

    def __init__(self, count: IncludeSupportingDocumentsClass, value: PurpleValue, next_link: IncludeSupportingDocumentsClass) -> None:
        self.count = count
        self.value = value
        self.next_link = next_link


class TrackerODataResponseOfAPBatchModel:
    type: APBatchModelType
    properties: TrackerODataResponseOfAPBatchModelProperties

    def __init__(self, type: APBatchModelType, properties: TrackerODataResponseOfAPBatchModelProperties) -> None:
        self.type = type
        self.properties = properties


class FluffyValue:
    type: ApRouteIDType
    items: ApBatchRunModel

    def __init__(self, type: ApRouteIDType, items: ApBatchRunModel) -> None:
        self.type = type
        self.items = items


class TrackerODataResponseOfAPBatchRunModelProperties:
    count: IncludeSupportingDocumentsClass
    value: FluffyValue
    next_link: IncludeSupportingDocumentsClass

    def __init__(self, count: IncludeSupportingDocumentsClass, value: FluffyValue, next_link: IncludeSupportingDocumentsClass) -> None:
        self.count = count
        self.value = value
        self.next_link = next_link


class TrackerODataResponseOfAPBatchRunModel:
    type: APBatchModelType
    properties: TrackerODataResponseOfAPBatchRunModelProperties

    def __init__(self, type: APBatchModelType, properties: TrackerODataResponseOfAPBatchRunModelProperties) -> None:
        self.type = type
        self.properties = properties


class TentacledValue:
    type: ApRouteIDType
    items: APRouteModelClass

    def __init__(self, type: ApRouteIDType, items: APRouteModelClass) -> None:
        self.type = type
        self.items = items


class TrackerODataResponseOfAPRouteModelProperties:
    count: IncludeSupportingDocumentsClass
    value: TentacledValue
    next_link: IncludeSupportingDocumentsClass

    def __init__(self, count: IncludeSupportingDocumentsClass, value: TentacledValue, next_link: IncludeSupportingDocumentsClass) -> None:
        self.count = count
        self.value = value
        self.next_link = next_link


class TrackerODataResponseOfAPRouteModel:
    type: APBatchModelType
    properties: TrackerODataResponseOfAPRouteModelProperties

    def __init__(self, type: APBatchModelType, properties: TrackerODataResponseOfAPRouteModelProperties) -> None:
        self.type = type
        self.properties = properties


class StickyValue:
    type: ApRouteIDType
    items: InvoicePaymentModel

    def __init__(self, type: ApRouteIDType, items: InvoicePaymentModel) -> None:
        self.type = type
        self.items = items


class TrackerODataResponseOfInvoicePaymentModelProperties:
    count: IncludeSupportingDocumentsClass
    value: StickyValue
    next_link: IncludeSupportingDocumentsClass

    def __init__(self, count: IncludeSupportingDocumentsClass, value: StickyValue, next_link: IncludeSupportingDocumentsClass) -> None:
        self.count = count
        self.value = value
        self.next_link = next_link


class TrackerODataResponseOfInvoicePaymentModel:
    type: APBatchModelType
    properties: TrackerODataResponseOfInvoicePaymentModelProperties

    def __init__(self, type: APBatchModelType, properties: TrackerODataResponseOfInvoicePaymentModelProperties) -> None:
        self.type = type
        self.properties = properties


class TransferCodingHeaderValueProperties:
    value: PaymentComments
    parameters: NoCacheHeaders

    def __init__(self, value: PaymentComments, parameters: NoCacheHeaders) -> None:
        self.value = value
        self.parameters = parameters


class TransferCodingHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: TransferCodingHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: TransferCodingHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class TransferCodingWithQualityHeaderValueProperties:
    value: PaymentComments
    parameters: NoCacheHeaders
    quality: Extensions

    def __init__(self, value: PaymentComments, parameters: NoCacheHeaders, quality: Extensions) -> None:
        self.value = value
        self.parameters = parameters
        self.quality = quality


class TransferCodingWithQualityHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: TransferCodingWithQualityHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: TransferCodingWithQualityHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class VersionProperties:
    major: InvoiceCountClass
    minor: InvoiceCountClass
    build: InvoiceCountClass
    revision: InvoiceCountClass
    major_revision: IncludeSupportingDocumentsClass
    minor_revision: IncludeSupportingDocumentsClass

    def __init__(self, major: InvoiceCountClass, minor: InvoiceCountClass, build: InvoiceCountClass, revision: InvoiceCountClass, major_revision: IncludeSupportingDocumentsClass, minor_revision: IncludeSupportingDocumentsClass) -> None:
        self.major = major
        self.minor = minor
        self.build = build
        self.revision = revision
        self.major_revision = major_revision
        self.minor_revision = minor_revision


class Version:
    type: APBatchModelType
    additional_properties: bool
    properties: VersionProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: VersionProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class ViaHeaderValueProperties:
    protocol_name: PaymentComments
    protocol_version: PaymentComments
    received_by: PaymentComments
    comment: PaymentComments

    def __init__(self, protocol_name: PaymentComments, protocol_version: PaymentComments, received_by: PaymentComments, comment: PaymentComments) -> None:
        self.protocol_name = protocol_name
        self.protocol_version = protocol_version
        self.received_by = received_by
        self.comment = comment


class ViaHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: ViaHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: ViaHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class WarningHeaderValueProperties:
    code: InvoiceCountClass
    agent: PaymentComments
    text: PaymentComments
    date: AccountID

    def __init__(self, code: InvoiceCountClass, agent: PaymentComments, text: PaymentComments, date: AccountID) -> None:
        self.code = code
        self.agent = agent
        self.text = text
        self.date = date


class WarningHeaderValue:
    type: APBatchModelType
    additional_properties: bool
    properties: WarningHeaderValueProperties

    def __init__(self, type: APBatchModelType, additional_properties: bool, properties: WarningHeaderValueProperties) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.properties = properties


class Schemas:
    ap_batch_model: ApBatchModel
    ap_extract_allowed_batch_payment_statuses: ApDataFileFormat
    tracker_o_data_response_of_ap_batch_model: TrackerODataResponseOfAPBatchModel
    error_response: ErrorResponse
    o_data_query_options_of_ap_batch_model: ApplyQueryOption
    http_request_message: HTTPRequestMessage
    version: Version
    http_content: HTTPContent
    http_content_headers: HTTPContentHeaders
    content_disposition_header_value: ContentDispositionHeaderValue
    name_value_header_value: NameValueHeaderValue
    content_range_header_value: ContentRangeHeaderValue
    media_type_header_value: MediaTypeHeaderValue
    http_method: HTTPMethod
    http_request_headers: HTTPRequestHeaders
    media_type_with_quality_header_value: MediaTypeHeaderValue
    string_with_quality_header_value: StringWithQualityHeaderValue
    authentication_header_value: AuthenticationHeaderValue
    name_value_with_parameters_header_value: NameValueWithParametersHeaderValue
    entity_tag_header_value: EntityTagHeaderValue
    range_condition_header_value: RangeConditionHeaderValue
    range_header_value: RangeHeaderValue
    range_item_header_value: RangeItemHeaderValue
    transfer_coding_with_quality_header_value: TransferCodingWithQualityHeaderValue
    product_info_header_value: ProductInfoHeaderValue
    product_header_value: ProductHeaderValue
    cache_control_header_value: CacheControlHeaderValue
    transfer_coding_header_value: TransferCodingHeaderValue
    via_header_value: ViaHeaderValue
    warning_header_value: WarningHeaderValue
    o_data_query_context: CountQueryOption
    default_query_settings: ApplyClause
    i_edm_model: ApplyQueryOption
    i_edm_schema_element: ApplyQueryOption
    edm_schema_element_kind: EdmContainerElementKind
    i_edm_vocabulary_annotation: CountQueryOption
    i_edm_term: ApplyQueryOption
    i_edm_type_reference: ApplyQueryOption
    i_edm_type: ApplyQueryOption
    edm_type_kind: EdmContainerElementKind
    i_edm_vocabulary_annotatable: CountQueryOption
    i_edm_expression: ApplyQueryOption
    edm_expression_kind: EdmContainerElementKind
    i_edm_direct_value_annotations_manager: ApplyQueryOption
    i_edm_entity_container: ApplyQueryOption
    i_edm_entity_container_element: ApplyQueryOption
    edm_container_element_kind: EdmContainerElementKind
    i_edm_navigation_source: ApplyQueryOption
    i_edm_navigation_property_binding: ApplyQueryOption
    i_edm_navigation_property: ApplyQueryOption
    edm_on_delete_action: EdmContainerElementKind
    i_edm_referential_constraint: ApplyQueryOption
    edm_referential_constraint_property_pair: ApplyClause
    i_edm_structural_property: ApplyQueryOption
    i_edm_path_expression: ApplyQueryOption
    o_data_path: ApplyClause
    o_data_path_segment: ApplyQueryOption
    i_service_provider: HTTPContent
    o_data_raw_query_options: ApplyClause
    select_expand_query_option: ApplyClause
    select_expand_query_validator: ApplyQueryOption
    select_expand_clause: CountQueryOption
    select_item: ApplyQueryOption
    apply_query_option: ApplyQueryOption
    apply_clause: ApplyClause
    transformation_node: ApplyQueryOption
    filter_query_option: ApplyClause
    filter_query_validator: ApplyClause
    filter_clause: ApplyClause
    single_value_node: ApplyQueryOption
    query_node_kind: EdmContainerElementKind
    range_variable: HTTPContent
    order_by_query_option: ApplyClause
    order_by_node: CountQueryOption
    order_by_direction: EdmContainerElementKind
    order_by_query_validator: ApplyQueryOption
    order_by_clause: ApplyQueryOption
    skip_query_option: HTTPContent
    skip_query_validator: HTTPContent
    skip_token_query_option: HTTPContent
    skip_token_query_validator: CountQueryOption
    o_data_query_settings: CountQueryOption
    handle_null_propagation_option: EdmContainerElementKind
    o_data_query_options: ApplyClause
    top_query_option: ApplyClause
    top_query_validator: ApplyClause
    count_query_option: CountQueryOption
    count_query_validator: ApplyClause
    o_data_query_validator: ApplyClause
    e_tag: ApplyClause
    e_tag_of_ap_batch_model: ApplyClause
    ap_batch_run_model: ApBatchRunModel
    tracker_o_data_response_of_ap_batch_run_model: TrackerODataResponseOfAPBatchRunModel
    o_data_query_options_of_ap_batch_run_model: CountQueryOption
    e_tag_of_ap_batch_run_model: ApplyClause
    ap_batch_payment_model: APBatchPaymentModel
    tap_extract_allowed_batch_payment_statuses: ApDataFileFormat
    ap_data_exchange_file_model: APDataExchangeFileModel
    ap_data_exchange_file_request: APDataExchangeFileRequest
    ap_data_file_type: ApDataFileFormat
    ap_data_file_format: ApDataFileFormat
    t_pdf_orientation: ApDataFileFormat
    t_font_size: EdmContainerElementKind
    ap_route_model: APRouteModelClass
    ap_route_email_model: ApRouteModel
    ap_route_sftp_model: ApRouteModel
    ap_route_web_service_model: APRouteWebServiceModel
    tracker_o_data_response_of_ap_route_model: TrackerODataResponseOfAPRouteModel
    recipient_email_model: RecipientEmailModel
    recipient_role: ApDataFileFormat
    recipient_type: ApDataFileFormat
    invoice_payment_model: InvoicePaymentModel
    tracker_o_data_response_of_invoice_payment_model: TrackerODataResponseOfInvoicePaymentModel
    payment_model: PaymentModel

    def __init__(self, ap_batch_model: ApBatchModel, ap_extract_allowed_batch_payment_statuses: ApDataFileFormat, tracker_o_data_response_of_ap_batch_model: TrackerODataResponseOfAPBatchModel, error_response: ErrorResponse, o_data_query_options_of_ap_batch_model: ApplyQueryOption, http_request_message: HTTPRequestMessage, version: Version, http_content: HTTPContent, http_content_headers: HTTPContentHeaders, content_disposition_header_value: ContentDispositionHeaderValue, name_value_header_value: NameValueHeaderValue, content_range_header_value: ContentRangeHeaderValue, media_type_header_value: MediaTypeHeaderValue, http_method: HTTPMethod, http_request_headers: HTTPRequestHeaders, media_type_with_quality_header_value: MediaTypeHeaderValue, string_with_quality_header_value: StringWithQualityHeaderValue, authentication_header_value: AuthenticationHeaderValue, name_value_with_parameters_header_value: NameValueWithParametersHeaderValue, entity_tag_header_value: EntityTagHeaderValue, range_condition_header_value: RangeConditionHeaderValue, range_header_value: RangeHeaderValue, range_item_header_value: RangeItemHeaderValue, transfer_coding_with_quality_header_value: TransferCodingWithQualityHeaderValue, product_info_header_value: ProductInfoHeaderValue, product_header_value: ProductHeaderValue, cache_control_header_value: CacheControlHeaderValue, transfer_coding_header_value: TransferCodingHeaderValue, via_header_value: ViaHeaderValue, warning_header_value: WarningHeaderValue, o_data_query_context: CountQueryOption, default_query_settings: ApplyClause, i_edm_model: ApplyQueryOption, i_edm_schema_element: ApplyQueryOption, edm_schema_element_kind: EdmContainerElementKind, i_edm_vocabulary_annotation: CountQueryOption, i_edm_term: ApplyQueryOption, i_edm_type_reference: ApplyQueryOption, i_edm_type: ApplyQueryOption, edm_type_kind: EdmContainerElementKind, i_edm_vocabulary_annotatable: CountQueryOption, i_edm_expression: ApplyQueryOption, edm_expression_kind: EdmContainerElementKind, i_edm_direct_value_annotations_manager: ApplyQueryOption, i_edm_entity_container: ApplyQueryOption, i_edm_entity_container_element: ApplyQueryOption, edm_container_element_kind: EdmContainerElementKind, i_edm_navigation_source: ApplyQueryOption, i_edm_navigation_property_binding: ApplyQueryOption, i_edm_navigation_property: ApplyQueryOption, edm_on_delete_action: EdmContainerElementKind, i_edm_referential_constraint: ApplyQueryOption, edm_referential_constraint_property_pair: ApplyClause, i_edm_structural_property: ApplyQueryOption, i_edm_path_expression: ApplyQueryOption, o_data_path: ApplyClause, o_data_path_segment: ApplyQueryOption, i_service_provider: HTTPContent, o_data_raw_query_options: ApplyClause, select_expand_query_option: ApplyClause, select_expand_query_validator: ApplyQueryOption, select_expand_clause: CountQueryOption, select_item: ApplyQueryOption, apply_query_option: ApplyQueryOption, apply_clause: ApplyClause, transformation_node: ApplyQueryOption, filter_query_option: ApplyClause, filter_query_validator: ApplyClause, filter_clause: ApplyClause, single_value_node: ApplyQueryOption, query_node_kind: EdmContainerElementKind, range_variable: HTTPContent, order_by_query_option: ApplyClause, order_by_node: CountQueryOption, order_by_direction: EdmContainerElementKind, order_by_query_validator: ApplyQueryOption, order_by_clause: ApplyQueryOption, skip_query_option: HTTPContent, skip_query_validator: HTTPContent, skip_token_query_option: HTTPContent, skip_token_query_validator: CountQueryOption, o_data_query_settings: CountQueryOption, handle_null_propagation_option: EdmContainerElementKind, o_data_query_options: ApplyClause, top_query_option: ApplyClause, top_query_validator: ApplyClause, count_query_option: CountQueryOption, count_query_validator: ApplyClause, o_data_query_validator: ApplyClause, e_tag: ApplyClause, e_tag_of_ap_batch_model: ApplyClause, ap_batch_run_model: ApBatchRunModel, tracker_o_data_response_of_ap_batch_run_model: TrackerODataResponseOfAPBatchRunModel, o_data_query_options_of_ap_batch_run_model: CountQueryOption, e_tag_of_ap_batch_run_model: ApplyClause, ap_batch_payment_model: APBatchPaymentModel, tap_extract_allowed_batch_payment_statuses: ApDataFileFormat, ap_data_exchange_file_model: APDataExchangeFileModel, ap_data_exchange_file_request: APDataExchangeFileRequest, ap_data_file_type: ApDataFileFormat, ap_data_file_format: ApDataFileFormat, t_pdf_orientation: ApDataFileFormat, t_font_size: EdmContainerElementKind, ap_route_model: APRouteModelClass, ap_route_email_model: ApRouteModel, ap_route_sftp_model: ApRouteModel, ap_route_web_service_model: APRouteWebServiceModel, tracker_o_data_response_of_ap_route_model: TrackerODataResponseOfAPRouteModel, recipient_email_model: RecipientEmailModel, recipient_role: ApDataFileFormat, recipient_type: ApDataFileFormat, invoice_payment_model: InvoicePaymentModel, tracker_o_data_response_of_invoice_payment_model: TrackerODataResponseOfInvoicePaymentModel, payment_model: PaymentModel) -> None:
        self.ap_batch_model = ap_batch_model
        self.ap_extract_allowed_batch_payment_statuses = ap_extract_allowed_batch_payment_statuses
        self.tracker_o_data_response_of_ap_batch_model = tracker_o_data_response_of_ap_batch_model
        self.error_response = error_response
        self.o_data_query_options_of_ap_batch_model = o_data_query_options_of_ap_batch_model
        self.http_request_message = http_request_message
        self.version = version
        self.http_content = http_content
        self.http_content_headers = http_content_headers
        self.content_disposition_header_value = content_disposition_header_value
        self.name_value_header_value = name_value_header_value
        self.content_range_header_value = content_range_header_value
        self.media_type_header_value = media_type_header_value
        self.http_method = http_method
        self.http_request_headers = http_request_headers
        self.media_type_with_quality_header_value = media_type_with_quality_header_value
        self.string_with_quality_header_value = string_with_quality_header_value
        self.authentication_header_value = authentication_header_value
        self.name_value_with_parameters_header_value = name_value_with_parameters_header_value
        self.entity_tag_header_value = entity_tag_header_value
        self.range_condition_header_value = range_condition_header_value
        self.range_header_value = range_header_value
        self.range_item_header_value = range_item_header_value
        self.transfer_coding_with_quality_header_value = transfer_coding_with_quality_header_value
        self.product_info_header_value = product_info_header_value
        self.product_header_value = product_header_value
        self.cache_control_header_value = cache_control_header_value
        self.transfer_coding_header_value = transfer_coding_header_value
        self.via_header_value = via_header_value
        self.warning_header_value = warning_header_value
        self.o_data_query_context = o_data_query_context
        self.default_query_settings = default_query_settings
        self.i_edm_model = i_edm_model
        self.i_edm_schema_element = i_edm_schema_element
        self.edm_schema_element_kind = edm_schema_element_kind
        self.i_edm_vocabulary_annotation = i_edm_vocabulary_annotation
        self.i_edm_term = i_edm_term
        self.i_edm_type_reference = i_edm_type_reference
        self.i_edm_type = i_edm_type
        self.edm_type_kind = edm_type_kind
        self.i_edm_vocabulary_annotatable = i_edm_vocabulary_annotatable
        self.i_edm_expression = i_edm_expression
        self.edm_expression_kind = edm_expression_kind
        self.i_edm_direct_value_annotations_manager = i_edm_direct_value_annotations_manager
        self.i_edm_entity_container = i_edm_entity_container
        self.i_edm_entity_container_element = i_edm_entity_container_element
        self.edm_container_element_kind = edm_container_element_kind
        self.i_edm_navigation_source = i_edm_navigation_source
        self.i_edm_navigation_property_binding = i_edm_navigation_property_binding
        self.i_edm_navigation_property = i_edm_navigation_property
        self.edm_on_delete_action = edm_on_delete_action
        self.i_edm_referential_constraint = i_edm_referential_constraint
        self.edm_referential_constraint_property_pair = edm_referential_constraint_property_pair
        self.i_edm_structural_property = i_edm_structural_property
        self.i_edm_path_expression = i_edm_path_expression
        self.o_data_path = o_data_path
        self.o_data_path_segment = o_data_path_segment
        self.i_service_provider = i_service_provider
        self.o_data_raw_query_options = o_data_raw_query_options
        self.select_expand_query_option = select_expand_query_option
        self.select_expand_query_validator = select_expand_query_validator
        self.select_expand_clause = select_expand_clause
        self.select_item = select_item
        self.apply_query_option = apply_query_option
        self.apply_clause = apply_clause
        self.transformation_node = transformation_node
        self.filter_query_option = filter_query_option
        self.filter_query_validator = filter_query_validator
        self.filter_clause = filter_clause
        self.single_value_node = single_value_node
        self.query_node_kind = query_node_kind
        self.range_variable = range_variable
        self.order_by_query_option = order_by_query_option
        self.order_by_node = order_by_node
        self.order_by_direction = order_by_direction
        self.order_by_query_validator = order_by_query_validator
        self.order_by_clause = order_by_clause
        self.skip_query_option = skip_query_option
        self.skip_query_validator = skip_query_validator
        self.skip_token_query_option = skip_token_query_option
        self.skip_token_query_validator = skip_token_query_validator
        self.o_data_query_settings = o_data_query_settings
        self.handle_null_propagation_option = handle_null_propagation_option
        self.o_data_query_options = o_data_query_options
        self.top_query_option = top_query_option
        self.top_query_validator = top_query_validator
        self.count_query_option = count_query_option
        self.count_query_validator = count_query_validator
        self.o_data_query_validator = o_data_query_validator
        self.e_tag = e_tag
        self.e_tag_of_ap_batch_model = e_tag_of_ap_batch_model
        self.ap_batch_run_model = ap_batch_run_model
        self.tracker_o_data_response_of_ap_batch_run_model = tracker_o_data_response_of_ap_batch_run_model
        self.o_data_query_options_of_ap_batch_run_model = o_data_query_options_of_ap_batch_run_model
        self.e_tag_of_ap_batch_run_model = e_tag_of_ap_batch_run_model
        self.ap_batch_payment_model = ap_batch_payment_model
        self.tap_extract_allowed_batch_payment_statuses = tap_extract_allowed_batch_payment_statuses
        self.ap_data_exchange_file_model = ap_data_exchange_file_model
        self.ap_data_exchange_file_request = ap_data_exchange_file_request
        self.ap_data_file_type = ap_data_file_type
        self.ap_data_file_format = ap_data_file_format
        self.t_pdf_orientation = t_pdf_orientation
        self.t_font_size = t_font_size
        self.ap_route_model = ap_route_model
        self.ap_route_email_model = ap_route_email_model
        self.ap_route_sftp_model = ap_route_sftp_model
        self.ap_route_web_service_model = ap_route_web_service_model
        self.tracker_o_data_response_of_ap_route_model = tracker_o_data_response_of_ap_route_model
        self.recipient_email_model = recipient_email_model
        self.recipient_role = recipient_role
        self.recipient_type = recipient_type
        self.invoice_payment_model = invoice_payment_model
        self.tracker_o_data_response_of_invoice_payment_model = tracker_o_data_response_of_invoice_payment_model
        self.payment_model = payment_model


class Scopes:
    access: str

    def __init__(self, access: str) -> None:
        self.access = access


class ClientCredentials:
    token_url: str
    scopes: Scopes

    def __init__(self, token_url: str, scopes: Scopes) -> None:
        self.token_url = token_url
        self.scopes = scopes


class Flows:
    client_credentials: ClientCredentials

    def __init__(self, client_credentials: ClientCredentials) -> None:
        self.client_credentials = client_credentials


class OAuth2:
    type: str
    flows: Flows

    def __init__(self, type: str, flows: Flows) -> None:
        self.type = type
        self.flows = flows


class SecuritySchemes:
    o_auth2: OAuth2

    def __init__(self, o_auth2: OAuth2) -> None:
        self.o_auth2 = o_auth2


class Components:
    schemas: Schemas
    security_schemes: SecuritySchemes

    def __init__(self, schemas: Schemas, security_schemes: SecuritySchemes) -> None:
        self.schemas = schemas
        self.security_schemes = security_schemes


class Info:
    title: str
    description: str
    version: str

    def __init__(self, title: str, description: str, version: str) -> None:
        self.title = title
        self.description = description
        self.version = version


class In(Enum):
    PATH = "path"
    QUERY = "query"


class PurpleParameter:
    name: str
    parameter_in: In
    description: str
    schema: IncludeSupportingDocumentsClass

    def __init__(self, name: str, parameter_in: In, description: str, schema: IncludeSupportingDocumentsClass) -> None:
        self.name = name
        self.parameter_in = parameter_in
        self.description = description
        self.schema = schema


class Code(Enum):
    UNAUTHORIZED = "Unauthorized"


class Message(Enum):
    THE_REQUESTED_RESOURCE_REQUIRES_AUTHENTICATION = "The requested resource requires authentication."


class ValueError:
    code: Code
    message: Message

    def __init__(self, code: Code, message: Message) -> None:
        self.code = code
        self.message = message


class AccessIsDeniedValue:
    error: ValueError

    def __init__(self, error: ValueError) -> None:
        self.error = error


class AccessIsDenied:
    value: AccessIsDeniedValue

    def __init__(self, value: AccessIsDeniedValue) -> None:
        self.value = value


class Examples:
    access_is_denied: AccessIsDenied

    def __init__(self, access_is_denied: AccessIsDenied) -> None:
        self.access_is_denied = access_is_denied


class PurpleApplicationJSON:
    schema: FileFormatClass
    examples: Optional[Examples]

    def __init__(self, schema: FileFormatClass, examples: Optional[Examples]) -> None:
        self.schema = schema
        self.examples = examples


class PurpleContent:
    application_json: PurpleApplicationJSON

    def __init__(self, application_json: PurpleApplicationJSON) -> None:
        self.application_json = application_json


class PatchResponse:
    description: str
    content: Optional[PurpleContent]

    def __init__(self, description: str, content: Optional[PurpleContent]) -> None:
        self.description = description
        self.content = content


class Security:
    o_auth2: List[Any]

    def __init__(self, o_auth2: List[Any]) -> None:
        self.o_auth2 = o_auth2


class InvoicesGet:
    tags: List[str]
    operation_id: str
    parameters: List[PurpleParameter]
    responses: Dict[str, PatchResponse]
    security: List[Security]

    def __init__(self, tags: List[str], operation_id: str, parameters: List[PurpleParameter], responses: Dict[str, PatchResponse], security: List[Security]) -> None:
        self.tags = tags
        self.operation_id = operation_id
        self.parameters = parameters
        self.responses = responses
        self.security = security


class Invoices:
    get: InvoicesGet

    def __init__(self, get: InvoicesGet) -> None:
        self.get = get


class ParameterSchema:
    type: ApRouteIDType
    format: Optional[Format]
    example: Optional[str]

    def __init__(self, type: ApRouteIDType, format: Optional[Format], example: Optional[str]) -> None:
        self.type = type
        self.format = format
        self.example = example


class FluffyParameter:
    name: str
    parameter_in: str
    required: Optional[bool]
    schema: ParameterSchema
    x_position: Optional[int]
    description: Optional[str]

    def __init__(self, name: str, parameter_in: str, required: Optional[bool], schema: ParameterSchema, x_position: Optional[int], description: Optional[str]) -> None:
        self.name = name
        self.parameter_in = parameter_in
        self.required = required
        self.schema = schema
        self.x_position = x_position
        self.description = description


class FluffyApplicationJSON:
    schema: FontSizeClass

    def __init__(self, schema: FontSizeClass) -> None:
        self.schema = schema


class RequestBodyContent:
    application_json: FluffyApplicationJSON

    def __init__(self, application_json: FluffyApplicationJSON) -> None:
        self.application_json = application_json


class RequestBody:
    x_name: str
    content: RequestBodyContent
    x_position: int

    def __init__(self, x_name: str, content: RequestBodyContent, x_position: int) -> None:
        self.x_name = x_name
        self.content = content
        self.x_position = x_position


class InvoicesInvoiceIDPatch:
    tags: List[str]
    operation_id: str
    parameters: List[FluffyParameter]
    request_body: RequestBody
    responses: Dict[str, PatchResponse]
    security: List[Security]

    def __init__(self, tags: List[str], operation_id: str, parameters: List[FluffyParameter], request_body: RequestBody, responses: Dict[str, PatchResponse], security: List[Security]) -> None:
        self.tags = tags
        self.operation_id = operation_id
        self.parameters = parameters
        self.request_body = request_body
        self.responses = responses
        self.security = security


class InvoicesInvoiceID:
    patch: InvoicesInvoiceIDPatch

    def __init__(self, patch: InvoicesInvoiceIDPatch) -> None:
        self.patch = patch


class TentacledParameter:
    name: str
    parameter_in: In
    required: bool
    schema: InvoiceCountClass
    x_position: int

    def __init__(self, name: str, parameter_in: In, required: bool, schema: InvoiceCountClass, x_position: int) -> None:
        self.name = name
        self.parameter_in = parameter_in
        self.required = required
        self.schema = schema
        self.x_position = x_position


class PostResponse:
    description: str
    content: PurpleContent

    def __init__(self, description: str, content: PurpleContent) -> None:
        self.description = description
        self.content = content


class InvoicesInvoiceIDFilesPost:
    tags: List[str]
    operation_id: str
    parameters: List[TentacledParameter]
    request_body: Optional[RequestBody]
    responses: Dict[str, PostResponse]
    security: List[Security]

    def __init__(self, tags: List[str], operation_id: str, parameters: List[TentacledParameter], request_body: Optional[RequestBody], responses: Dict[str, PostResponse], security: List[Security]) -> None:
        self.tags = tags
        self.operation_id = operation_id
        self.parameters = parameters
        self.request_body = request_body
        self.responses = responses
        self.security = security


class InvoicesInvoiceIDFiles:
    post: InvoicesInvoiceIDFilesPost

    def __init__(self, post: InvoicesInvoiceIDFilesPost) -> None:
        self.post = post


class InvoicesInvoiceIDSpreadsheet:
    get: InvoicesInvoiceIDFilesPost

    def __init__(self, get: InvoicesInvoiceIDFilesPost) -> None:
        self.get = get


class StickyParameter:
    name: str
    parameter_in: In
    required: Optional[bool]
    schema: InvoiceCountClass
    x_position: Optional[int]
    description: Optional[str]

    def __init__(self, name: str, parameter_in: In, required: Optional[bool], schema: InvoiceCountClass, x_position: Optional[int], description: Optional[str]) -> None:
        self.name = name
        self.parameter_in = parameter_in
        self.required = required
        self.schema = schema
        self.x_position = x_position
        self.description = description


class RoutesRouteIDBatchesGet:
    tags: List[str]
    operation_id: str
    parameters: List[StickyParameter]
    responses: Dict[str, PatchResponse]
    security: List[Security]

    def __init__(self, tags: List[str], operation_id: str, parameters: List[StickyParameter], responses: Dict[str, PatchResponse], security: List[Security]) -> None:
        self.tags = tags
        self.operation_id = operation_id
        self.parameters = parameters
        self.responses = responses
        self.security = security


class RoutesRouteIDBatches:
    get: RoutesRouteIDBatchesGet

    def __init__(self, get: RoutesRouteIDBatchesGet) -> None:
        self.get = get


class IndigoParameter:
    name: str
    parameter_in: str
    required: Optional[bool]
    schema: Extensions
    x_position: Optional[int]
    description: Optional[str]

    def __init__(self, name: str, parameter_in: str, required: Optional[bool], schema: Extensions, x_position: Optional[int], description: Optional[str]) -> None:
        self.name = name
        self.parameter_in = parameter_in
        self.required = required
        self.schema = schema
        self.x_position = x_position
        self.description = description


class RoutesRouteIDBatchesBatchIDPatch:
    tags: List[str]
    operation_id: str
    parameters: List[IndigoParameter]
    request_body: RequestBody
    responses: Dict[str, PatchResponse]
    security: List[Security]

    def __init__(self, tags: List[str], operation_id: str, parameters: List[IndigoParameter], request_body: RequestBody, responses: Dict[str, PatchResponse], security: List[Security]) -> None:
        self.tags = tags
        self.operation_id = operation_id
        self.parameters = parameters
        self.request_body = request_body
        self.responses = responses
        self.security = security


class RoutesRouteIDBatchesBatchID:
    patch: RoutesRouteIDBatchesBatchIDPatch

    def __init__(self, patch: RoutesRouteIDBatchesBatchIDPatch) -> None:
        self.patch = patch


class IndecentParameter:
    name: str
    parameter_in: In
    required: Optional[bool]
    schema: AccountID
    x_position: Optional[int]
    description: Optional[str]

    def __init__(self, name: str, parameter_in: In, required: Optional[bool], schema: AccountID, x_position: Optional[int], description: Optional[str]) -> None:
        self.name = name
        self.parameter_in = parameter_in
        self.required = required
        self.schema = schema
        self.x_position = x_position
        self.description = description


class RoutesRouteIDBatchesBatchIDFilesPost:
    tags: List[str]
    operation_id: str
    parameters: List[IndecentParameter]
    request_body: Optional[RequestBody]
    responses: Dict[str, PostResponse]
    security: List[Security]

    def __init__(self, tags: List[str], operation_id: str, parameters: List[IndecentParameter], request_body: Optional[RequestBody], responses: Dict[str, PostResponse], security: List[Security]) -> None:
        self.tags = tags
        self.operation_id = operation_id
        self.parameters = parameters
        self.request_body = request_body
        self.responses = responses
        self.security = security


class RoutesRouteIDBatchesBatchIDFiles:
    post: RoutesRouteIDBatchesBatchIDFilesPost

    def __init__(self, post: RoutesRouteIDBatchesBatchIDFilesPost) -> None:
        self.post = post


class RoutesRouteIDBatchesBatchIDRunsGet:
    tags: List[str]
    operation_id: str
    parameters: List[IndecentParameter]
    responses: Dict[str, PatchResponse]
    security: List[Security]

    def __init__(self, tags: List[str], operation_id: str, parameters: List[IndecentParameter], responses: Dict[str, PatchResponse], security: List[Security]) -> None:
        self.tags = tags
        self.operation_id = operation_id
        self.parameters = parameters
        self.responses = responses
        self.security = security


class RoutesRouteIDBatchesBatchIDRuns:
    get: RoutesRouteIDBatchesBatchIDRunsGet

    def __init__(self, get: RoutesRouteIDBatchesBatchIDRunsGet) -> None:
        self.get = get


class RoutesRouteIDBatchesBatchIDSpreadsheet:
    get: RoutesRouteIDBatchesBatchIDFilesPost

    def __init__(self, get: RoutesRouteIDBatchesBatchIDFilesPost) -> None:
        self.get = get


class ApplicationJSONSchema:
    type: Optional[ApRouteIDType]
    items: Optional[FileFormatClass]
    ref: Optional[str]

    def __init__(self, type: Optional[ApRouteIDType], items: Optional[FileFormatClass], ref: Optional[str]) -> None:
        self.type = type
        self.items = items
        self.ref = ref


class TentacledApplicationJSON:
    schema: ApplicationJSONSchema
    examples: Optional[Examples]

    def __init__(self, schema: ApplicationJSONSchema, examples: Optional[Examples]) -> None:
        self.schema = schema
        self.examples = examples


class FluffyContent:
    application_json: TentacledApplicationJSON

    def __init__(self, application_json: TentacledApplicationJSON) -> None:
        self.application_json = application_json


class PurpleResponse:
    description: str
    content: FluffyContent

    def __init__(self, description: str, content: FluffyContent) -> None:
        self.description = description
        self.content = content


class RoutesRouteIDEmailRecipientsGet:
    tags: List[str]
    operation_id: str
    parameters: List[TentacledParameter]
    responses: Dict[str, PurpleResponse]
    security: List[Security]

    def __init__(self, tags: List[str], operation_id: str, parameters: List[TentacledParameter], responses: Dict[str, PurpleResponse], security: List[Security]) -> None:
        self.tags = tags
        self.operation_id = operation_id
        self.parameters = parameters
        self.responses = responses
        self.security = security


class RoutesRouteIDEmailRecipients:
    get: RoutesRouteIDEmailRecipientsGet

    def __init__(self, get: RoutesRouteIDEmailRecipientsGet) -> None:
        self.get = get


class Paths:
    routes_route_id_batches: RoutesRouteIDBatches
    routes_route_id_batches_batch_id_runs: RoutesRouteIDBatchesBatchIDRuns
    routes_route_id_batches_batch_id: RoutesRouteIDBatchesBatchID
    routes_route_id_batches_batch_id_files: RoutesRouteIDBatchesBatchIDFiles
    routes_route_id_batches_batch_id_spreadsheet: RoutesRouteIDBatchesBatchIDSpreadsheet
    routes: Invoices
    routes_route_id_email_recipients: RoutesRouteIDEmailRecipients
    invoices: Invoices
    invoices_invoice_id: InvoicesInvoiceID
    invoices_invoice_id_spreadsheet: InvoicesInvoiceIDSpreadsheet
    invoices_invoice_id_files: InvoicesInvoiceIDFiles

    def __init__(self, routes_route_id_batches: RoutesRouteIDBatches, routes_route_id_batches_batch_id_runs: RoutesRouteIDBatchesBatchIDRuns, routes_route_id_batches_batch_id: RoutesRouteIDBatchesBatchID, routes_route_id_batches_batch_id_files: RoutesRouteIDBatchesBatchIDFiles, routes_route_id_batches_batch_id_spreadsheet: RoutesRouteIDBatchesBatchIDSpreadsheet, routes: Invoices, routes_route_id_email_recipients: RoutesRouteIDEmailRecipients, invoices: Invoices, invoices_invoice_id: InvoicesInvoiceID, invoices_invoice_id_spreadsheet: InvoicesInvoiceIDSpreadsheet, invoices_invoice_id_files: InvoicesInvoiceIDFiles) -> None:
        self.routes_route_id_batches = routes_route_id_batches
        self.routes_route_id_batches_batch_id_runs = routes_route_id_batches_batch_id_runs
        self.routes_route_id_batches_batch_id = routes_route_id_batches_batch_id
        self.routes_route_id_batches_batch_id_files = routes_route_id_batches_batch_id_files
        self.routes_route_id_batches_batch_id_spreadsheet = routes_route_id_batches_batch_id_spreadsheet
        self.routes = routes
        self.routes_route_id_email_recipients = routes_route_id_email_recipients
        self.invoices = invoices
        self.invoices_invoice_id = invoices_invoice_id
        self.invoices_invoice_id_spreadsheet = invoices_invoice_id_spreadsheet
        self.invoices_invoice_id_files = invoices_invoice_id_files


class Server:
    url: str

    def __init__(self, url: str) -> None:
        self.url = url


class Tag:
    name: str
    description: str

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description


class Welcome7:
    x_generator: str
    openapi: str
    info: Info
    servers: List[Server]
    paths: Paths
    components: Components
    tags: List[Tag]

    def __init__(self, x_generator: str, openapi: str, info: Info, servers: List[Server], paths: Paths, components: Components, tags: List[Tag]) -> None:
        self.x_generator = x_generator
        self.openapi = openapi
        self.info = info
        self.servers = servers
        self.paths = paths
        self.components = components
        self.tags = tags


    @classmethod
    def from_json_file(cls, filename):

        with open(filename) as f:
            data = json.load(f)
        return cls(**data)

def main():
    person = Welcome7.from_json_file(r'C:\Users\User\Downloads\devportal-ap-exchange-api.v1.json')
    print(person)

main()


