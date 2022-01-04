from dataclasses import dataclass, field
import datetime as dt

@dataclass
class Sales_Orders:
    OrderID: int
    CustomerID: int
    SalepersonPersonID: int
    PickedByPersonID: int
    ContactPersonID: int
    BackorderOrderID: int
    OrderDate: dt.date 
    ExpectedDeliveryDate: dt.date
    CustomerPurchaseOrderNumber: str
    IsUnderSupplyBackordered: bool
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    PickingCompletedWhen: dt.datetime
    LastEditedBy: int
    LastEditedWhen: dt.datetime
    
    # The order doesn't have an amount in it directly so do a comparison based upon the
    # date of the order. If we want to compare based on total value we will need to access other datasets
    def __gt__(self, other):
        return self.OrderDate > other.OrderDate

    def __ge__(self, other):
        return self.OrderDate >= other.OrderDate
    
    def __eq__(self, other):
        return self.OrderDate == other.OrderDate

    
@dataclass
class Sales_Invoices:
    InvoiceID: int
    CustomerID: int
    BillToCustomerID: int
    OrderID: int
    DeliveryMethodID: int
    ContactPersonID: int
    AccountsPersonID: int
    SalespersonPersonID: int
    PackedByPersonID: int
    InvoiceDate: dt.datetime
    CustomerPurchaseOrderNumber: str
    IsCreditNote: bool
    CreditNoteReason: str
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    TotalDryItems: int
    TotalChillerItems: int
    DeliveryRun: str
    RunPosition: bool
    ReturnedDeliveryData: str
    ConfirmedDeliveryTime: dt.datetime
    ConfirmedReceivedBy: str
    LastEditedBy: int
    LastEditedWhen: dt.datetime
    
    # The invoice doesn't have an amount in it directly so do a comparison based upon the
    # date of the invoice. If we want to compare based on total value we will need to access other datasets
    def __gt__(self, other):
        return self.InvoiceDate > other.InvoiceDate

    def __ge__(self, other):
        return self.InvoiceDate >= other.InvoiceDate
    
    def __eq__(self, other):
        return self.InvoiceDate == other.InvoiceDate


@dataclass
class Sales_Customers:
    CustomerID: int
    CustomerName: str
    BillToCustomerID: int
    CustomerCategoryID: int
    BuyingGroupID: int
    PrimaryContactPersonID: int
    AlternateContactPersonID: int
    DeliveryMethodID: int
    DeliveryCityID: int
    PostalCityID: int
    CreditLimit: float
    AccountOpenedDate: dt.date
    StandardDiscountPercentage: float
    IsStatementSent: bool
    IsOnCreditHold: bool
    PaymentDays: int
    PhoneNumber: str
    FaxNumber: str
    DeliveryRun: str
    RunPosition: bool
    WebsiteURL: str
    DeliveryAddressLine1: str
    DeliveryAddressLine2: str
    DeliveryPostalCode: str
    DeliveryLocation: str
    PostalAddressLine1: str
    PostalAddressLine2: str
    PostalPostalCode: str
    LastEditedBy: int
    ValidFrom: dt.datetime
    ValidTo: dt.datetime

