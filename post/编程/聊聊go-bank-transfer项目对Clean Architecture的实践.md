
---
title: 聊聊go-bank-transfer项目对Clean Architecture的实践
categories: 
    - 编程
    - 掘金 - 标签
author: 掘金 - 标签
comments: false
date: Sun, 21 Mar 2021 05:45:20 GMT
thumbnail: 
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><h2 data-id="heading-0">序</h2>
<p>本文主要赏析一下go-bank-transfer对于 Clean Architecture的实践</p>
<h2 data-id="heading-1">项目结构</h2>
<pre><code class="copyable">├── adapter
│   ├── api
│   │   ├── action
│   │   ├── logging
│   │   ├── middleware
│   │   └── response
│   ├── logger
│   ├── presenter
│   ├── repository
│   └── validator
├── domain
├── infrastructure
│   ├── database
│   ├── log
│   ├── router
│   └── validation
└── usecase
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里分为adapter、domain、infrastructure、usecase四层</p>
</blockquote>
<h2 data-id="heading-2">domain</h2>
<h3 data-id="heading-3">account</h3>
<pre><code class="copyable">type AccountID string

func (a AccountID) String() string {
return string(a)
}

type (
AccountRepository interface {
Create(context.Context, Account) (Account, error)
UpdateBalance(context.Context, AccountID, Money) error
FindAll(context.Context) ([]Account, error)
FindByID(context.Context, AccountID) (Account, error)
FindBalance(context.Context, AccountID) (Account, error)
}

Account struct {
id        AccountID
name      string
cpf       string
balance   Money
createdAt time.Time
}
)

func NewAccount(ID AccountID, name, CPF string, balance Money, createdAt time.Time) Account {
return Account{
id:        ID,
name:      name,
cpf:       CPF,
balance:   balance,
createdAt: createdAt,
}
}

func (a *Account) Deposit(amount Money) {
a.balance += amount
}

func (a *Account) Withdraw(amount Money) error {
if a.balance < amount {
return ErrInsufficientBalance
}

a.balance -= amount

return nil
}

func (a Account) ID() AccountID {
return a.id
}

func (a Account) Name() string {
return a.name
}

func (a Account) CPF() string {
return a.cpf
}

func (a Account) Balance() Money {
return a.balance
}

func (a Account) CreatedAt() time.Time {
return a.createdAt
}

func NewAccountBalance(balance Money) Account {
return Account{balance: balance}
}
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>account定义了AccountRepository接口及Account类型，同时还提供了Withdraw、Deposit方法</p>
</blockquote>
<h3 data-id="heading-4">transfer</h3>
<pre><code class="copyable">type TransferID string

func (t TransferID) String() string {
return string(t)
}

type (
TransferRepository interface {
Create(context.Context, Transfer) (Transfer, error)
FindAll(context.Context) ([]Transfer, error)
WithTransaction(context.Context, func(context.Context) error) error
}

Transfer struct {
id                   TransferID
accountOriginID      AccountID
accountDestinationID AccountID
amount               Money
createdAt            time.Time
}
)

func NewTransfer(
ID TransferID,
accountOriginID AccountID,
accountDestinationID AccountID,
amount Money,
createdAt time.Time,
) Transfer {
return Transfer{
id:                   ID,
accountOriginID:      accountOriginID,
accountDestinationID: accountDestinationID,
amount:               amount,
createdAt:            createdAt,
}
}

func (t Transfer) ID() TransferID {
return t.id
}

func (t Transfer) AccountOriginID() AccountID {
return t.accountOriginID
}

func (t Transfer) AccountDestinationID() AccountID {
return t.accountDestinationID
}

func (t Transfer) Amount() Money {
return t.amount
}

func (t Transfer) CreatedAt() time.Time {
return t.createdAt
}
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>transfer定义了TransferRepository接口及Transfer类型</p>
</blockquote>
<h2 data-id="heading-5">usecase</h2>
<pre><code class="copyable">➜  usecase git:(master) tree
.
├── create_account.go
├── create_account_test.go
├── create_transfer.go
├── create_transfer_test.go
├── find_account_balance.go
├── find_account_balance_test.go
├── find_all_account.go
├── find_all_account_test.go
├── find_all_transfer.go
└── find_all_transfer_test.go
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一层定义了CreateAccountUseCase与CreateAccountPresenter、CreateTransferUseCase与CreateTransferPresenter、FindAccountBalanceUseCase与FindAccountBalancePresenter、FindAllAccountUseCase与FindAllAccountPresenter、FindAllTransferUseCase与FindAllTransferPresenter接口</p>
<h2 data-id="heading-6">adapter</h2>
<pre><code class="copyable">➜  adapter git:(master) tree
.
├── api
│   ├── action
│   │   ├── create_account.go
│   │   ├── create_account_test.go
│   │   ├── create_transfer.go
│   │   ├── create_transfer_test.go
│   │   ├── find_account_balance.go
│   │   ├── find_account_balance_test.go
│   │   ├── find_all_account.go
│   │   ├── find_all_account_test.go
│   │   ├── find_all_transfer.go
│   │   ├── find_all_transfer_test.go
│   │   ├── health_check.go
│   │   └── health_check_test.go
│   ├── logging
│   │   ├── error.go
│   │   └── info.go
│   ├── middleware
│   │   └── logger.go
│   └── response
│       ├── error.go
│       └── success.go
├── logger
│   └── logger.go
├── presenter
│   ├── create_account.go
│   ├── create_account_test.go
│   ├── create_transfer.go
│   ├── create_transfer_test.go
│   ├── find_account_balance.go
│   ├── find_account_balance_test.go
│   ├── find_all_account.go
│   ├── find_all_account_test.go
│   ├── find_all_transfer.go
│   └── find_all_transfer_test.go
├── repository
│   ├── account_mongodb.go
│   ├── account_postgres.go
│   ├── nosql.go
│   ├── sql.go
│   ├── transfer_mongodb.go
│   └── transfer_postgres.go
└── validator
    └── validator.go
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>adapter层实现了domain与usecase层定义的接口</p>
</blockquote>
<h2 data-id="heading-7">小结</h2>
<p>go-bank-transfer工程在domain层定义了model及repository接口，usecase层定义了usecase及presenter接口，同时调用domain层实现业务编排；adapter则实现了上面两层定义的接口。</p>
<h2 data-id="heading-8">doc</h2>
<ul>
<li><a href="https://github.com/GSabadini/go-bank-transfer" target="_blank" rel="nofollow noopener noreferrer">go-bank-transfer</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            