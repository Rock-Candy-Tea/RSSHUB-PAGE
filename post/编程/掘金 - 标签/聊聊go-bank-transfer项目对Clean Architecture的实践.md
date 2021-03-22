
---
title: '聊聊go-bank-transfer项目对Clean Architecture的实践'
categories: 
    - 编程
    - 掘金 - 标签
author: 掘金 - 标签
comments: false
date: Sun, 21 Mar 2021 05:45:20 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">序</h2>
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

func (a AccountID) String() string &#123;
return string(a)
&#125;

type (
AccountRepository interface &#123;
Create(context.Context, Account) (Account, error)
UpdateBalance(context.Context, AccountID, Money) error
FindAll(context.Context) ([]Account, error)
FindByID(context.Context, AccountID) (Account, error)
FindBalance(context.Context, AccountID) (Account, error)
&#125;

Account struct &#123;
id        AccountID
name      string
cpf       string
balance   Money
createdAt time.Time
&#125;
)

func NewAccount(ID AccountID, name, CPF string, balance Money, createdAt time.Time) Account &#123;
return Account&#123;
id:        ID,
name:      name,
cpf:       CPF,
balance:   balance,
createdAt: createdAt,
&#125;
&#125;

func (a *Account) Deposit(amount Money) &#123;
a.balance += amount
&#125;

func (a *Account) Withdraw(amount Money) error &#123;
if a.balance < amount &#123;
return ErrInsufficientBalance
&#125;

a.balance -= amount

return nil
&#125;

func (a Account) ID() AccountID &#123;
return a.id
&#125;

func (a Account) Name() string &#123;
return a.name
&#125;

func (a Account) CPF() string &#123;
return a.cpf
&#125;

func (a Account) Balance() Money &#123;
return a.balance
&#125;

func (a Account) CreatedAt() time.Time &#123;
return a.createdAt
&#125;

func NewAccountBalance(balance Money) Account &#123;
return Account&#123;balance: balance&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>account定义了AccountRepository接口及Account类型，同时还提供了Withdraw、Deposit方法</p>
</blockquote>
<h3 data-id="heading-4">transfer</h3>
<pre><code class="copyable">type TransferID string

func (t TransferID) String() string &#123;
return string(t)
&#125;

type (
TransferRepository interface &#123;
Create(context.Context, Transfer) (Transfer, error)
FindAll(context.Context) ([]Transfer, error)
WithTransaction(context.Context, func(context.Context) error) error
&#125;

Transfer struct &#123;
id                   TransferID
accountOriginID      AccountID
accountDestinationID AccountID
amount               Money
createdAt            time.Time
&#125;
)

func NewTransfer(
ID TransferID,
accountOriginID AccountID,
accountDestinationID AccountID,
amount Money,
createdAt time.Time,
) Transfer &#123;
return Transfer&#123;
id:                   ID,
accountOriginID:      accountOriginID,
accountDestinationID: accountDestinationID,
amount:               amount,
createdAt:            createdAt,
&#125;
&#125;

func (t Transfer) ID() TransferID &#123;
return t.id
&#125;

func (t Transfer) AccountOriginID() AccountID &#123;
return t.accountOriginID
&#125;

func (t Transfer) AccountDestinationID() AccountID &#123;
return t.accountDestinationID
&#125;

func (t Transfer) Amount() Money &#123;
return t.amount
&#125;

func (t Transfer) CreatedAt() time.Time &#123;
return t.createdAt
&#125;
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
            