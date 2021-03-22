
---
title: 聊聊buckpal对于Hexagonal Architecture的实践
categories: 
    - 编程
    - 掘金 - 标签
author: 掘金 - 标签
comments: false
date: Sat, 20 Mar 2021 06:17:59 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">序</h2>
<p>本文主要赏析一下buckpal对于Hexagonal Architecture的实践</p>
<h2 data-id="heading-1">项目结构</h2>
<pre><code class="copyable">├── adapter
│   ├── in
│   │   └── web
│   │       └── SendMoneyController.java
│   └── out
│       └── persistence
│           ├── AccountJpaEntity.java
│           ├── AccountMapper.java
│           ├── AccountPersistenceAdapter.java
│           ├── ActivityJpaEntity.java
│           ├── ActivityRepository.java
│           └── SpringDataAccountRepository.java
├── application
│   ├── port
│   │   ├── in
│   │   │   ├── GetAccountBalanceQuery.java
│   │   │   ├── SendMoneyCommand.java
│   │   │   └── SendMoneyUseCase.java
│   │   └── out
│   │       ├── AccountLock.java
│   │       ├── LoadAccountPort.java
│   │       └── UpdateAccountStatePort.java
│   └── service
│       ├── GetAccountBalanceService.java
│       ├── MoneyTransferProperties.java
│       ├── NoOpAccountLock.java
│       ├── SendMoneyService.java
│       └── ThresholdExceededException.java
└── domain
    ├── Account.java
    ├── Activity.java
    ├── ActivityWindow.java
    └── Money.java
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里分为adapter、application、domain三层；其中application层定义了port包，该包定义了in、out两种类型的接口；adapter层也分in、out两类，分别实现application/port层的接口；application的service则实现了port的接口</p>
</blockquote>
<h2 data-id="heading-2">application/port</h2>
<h3 data-id="heading-3">in</h3>
<pre><code class="copyable">public interface GetAccountBalanceQuery &#123;

Money getAccountBalance(AccountId accountId);

&#125;

@Value
@EqualsAndHashCode(callSuper = false)
public
class SendMoneyCommand extends SelfValidating<SendMoneyCommand> &#123;

    @NotNull
    private final AccountId sourceAccountId;

    @NotNull
    private final AccountId targetAccountId;

    @NotNull
    private final Money money;

    public SendMoneyCommand(
            AccountId sourceAccountId,
            AccountId targetAccountId,
            Money money) &#123;
        this.sourceAccountId = sourceAccountId;
        this.targetAccountId = targetAccountId;
        this.money = money;
        this.validateSelf();
    &#125;
&#125;

public interface SendMoneyUseCase &#123;

boolean sendMoney(SendMoneyCommand command);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>application/port/in定义了GetAccountBalanceQuery、SendMoneyUseCase接口</p>
</blockquote>
<h3 data-id="heading-4">out</h3>
<pre><code class="copyable">public interface AccountLock &#123;

void lockAccount(Account.AccountId accountId);

void releaseAccount(Account.AccountId accountId);

&#125;

public interface LoadAccountPort &#123;

Account loadAccount(AccountId accountId, LocalDateTime baselineDate);
&#125;

public interface UpdateAccountStatePort &#123;

void updateActivities(Account account);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>application/port/out定义了AccountLock、LoadAccountPort、UpdateAccountStatePort接口</p>
</blockquote>
<h2 data-id="heading-5">application/service</h2>
<pre><code class="copyable">@RequiredArgsConstructor
class GetAccountBalanceService implements GetAccountBalanceQuery &#123;

private final LoadAccountPort loadAccountPort;

@Override
public Money getAccountBalance(AccountId accountId) &#123;
return loadAccountPort.loadAccount(accountId, LocalDateTime.now())
.calculateBalance();
&#125;
&#125;

@Component
class NoOpAccountLock implements AccountLock &#123;

@Override
public void lockAccount(AccountId accountId) &#123;
// do nothing
&#125;

@Override
public void releaseAccount(AccountId accountId) &#123;
// do nothing
&#125;

&#125;

@RequiredArgsConstructor
@UseCase
@Transactional
public class SendMoneyService implements SendMoneyUseCase &#123;

private final LoadAccountPort loadAccountPort;
private final AccountLock accountLock;
private final UpdateAccountStatePort updateAccountStatePort;
private final MoneyTransferProperties moneyTransferProperties;

@Override
public boolean sendMoney(SendMoneyCommand command) &#123;

checkThreshold(command);

LocalDateTime baselineDate = LocalDateTime.now().minusDays(10);

Account sourceAccount = loadAccountPort.loadAccount(
command.getSourceAccountId(),
baselineDate);

Account targetAccount = loadAccountPort.loadAccount(
command.getTargetAccountId(),
baselineDate);

AccountId sourceAccountId = sourceAccount.getId()
.orElseThrow(() -> new IllegalStateException("expected source account ID not to be empty"));
AccountId targetAccountId = targetAccount.getId()
.orElseThrow(() -> new IllegalStateException("expected target account ID not to be empty"));

accountLock.lockAccount(sourceAccountId);
if (!sourceAccount.withdraw(command.getMoney(), targetAccountId)) &#123;
accountLock.releaseAccount(sourceAccountId);
return false;
&#125;

accountLock.lockAccount(targetAccountId);
if (!targetAccount.deposit(command.getMoney(), sourceAccountId)) &#123;
accountLock.releaseAccount(sourceAccountId);
accountLock.releaseAccount(targetAccountId);
return false;
&#125;

updateAccountStatePort.updateActivities(sourceAccount);
updateAccountStatePort.updateActivities(targetAccount);

accountLock.releaseAccount(sourceAccountId);
accountLock.releaseAccount(targetAccountId);
return true;
&#125;

private void checkThreshold(SendMoneyCommand command) &#123;
if(command.getMoney().isGreaterThan(moneyTransferProperties.getMaximumTransferThreshold()))&#123;
throw new ThresholdExceededException(moneyTransferProperties.getMaximumTransferThreshold(), command.getMoney());
&#125;
&#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>application/service的GetAccountBalanceService实现了application.port.in.GetAccountBalanceQuery接口；NoOpAccountLock实现了application.port.out.AccountLock接口；SendMoneyService实现了application.port.in.SendMoneyUseCase接口</p>
</blockquote>
<h2 data-id="heading-6">domain</h2>
<pre><code class="copyable">@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class Account &#123;

/**
 * The unique ID of the account.
 */
@Getter private final AccountId id;

/**
 * The baseline balance of the account. This was the balance of the account before the first
 * activity in the activityWindow.
 */
@Getter private final Money baselineBalance;

/**
 * The window of latest activities on this account.
 */
@Getter private final ActivityWindow activityWindow;

/**
 * Creates an &#123;@link Account&#125; entity without an ID. Use to create a new entity that is not yet
 * persisted.
 */
public static Account withoutId(
Money baselineBalance,
ActivityWindow activityWindow) &#123;
return new Account(null, baselineBalance, activityWindow);
&#125;

/**
 * Creates an &#123;@link Account&#125; entity with an ID. Use to reconstitute a persisted entity.
 */
public static Account withId(
AccountId accountId,
Money baselineBalance,
ActivityWindow activityWindow) &#123;
return new Account(accountId, baselineBalance, activityWindow);
&#125;

public Optional<AccountId> getId()&#123;
return Optional.ofNullable(this.id);
&#125;

/**
 * Calculates the total balance of the account by adding the activity values to the baseline balance.
 */
public Money calculateBalance() &#123;
return Money.add(
this.baselineBalance,
this.activityWindow.calculateBalance(this.id));
&#125;

/**
 * Tries to withdraw a certain amount of money from this account.
 * If successful, creates a new activity with a negative value.
 * @return true if the withdrawal was successful, false if not.
 */
public boolean withdraw(Money money, AccountId targetAccountId) &#123;

if (!mayWithdraw(money)) &#123;
return false;
&#125;

Activity withdrawal = new Activity(
this.id,
this.id,
targetAccountId,
LocalDateTime.now(),
money);
this.activityWindow.addActivity(withdrawal);
return true;
&#125;

private boolean mayWithdraw(Money money) &#123;
return Money.add(
this.calculateBalance(),
money.negate())
.isPositiveOrZero();
&#125;

/**
 * Tries to deposit a certain amount of money to this account.
 * If sucessful, creates a new activity with a positive value.
 * @return true if the deposit was successful, false if not.
 */
public boolean deposit(Money money, AccountId sourceAccountId) &#123;
Activity deposit = new Activity(
this.id,
sourceAccountId,
this.id,
LocalDateTime.now(),
money);
this.activityWindow.addActivity(deposit);
return true;
&#125;

@Value
public static class AccountId &#123;
private Long value;
&#125;

&#125;

public class ActivityWindow &#123;

/**
 * The list of account activities within this window.
 */
private List<Activity> activities;

/**
 * The timestamp of the first activity within this window.
 */
public LocalDateTime getStartTimestamp() &#123;
return activities.stream()
.min(Comparator.comparing(Activity::getTimestamp))
.orElseThrow(IllegalStateException::new)
.getTimestamp();
&#125;

/**
 * The timestamp of the last activity within this window.
 * @return
 */
public LocalDateTime getEndTimestamp() &#123;
return activities.stream()
.max(Comparator.comparing(Activity::getTimestamp))
.orElseThrow(IllegalStateException::new)
.getTimestamp();
&#125;

/**
 * Calculates the balance by summing up the values of all activities within this window.
 */
public Money calculateBalance(AccountId accountId) &#123;
Money depositBalance = activities.stream()
.filter(a -> a.getTargetAccountId().equals(accountId))
.map(Activity::getMoney)
.reduce(Money.ZERO, Money::add);

Money withdrawalBalance = activities.stream()
.filter(a -> a.getSourceAccountId().equals(accountId))
.map(Activity::getMoney)
.reduce(Money.ZERO, Money::add);

return Money.add(depositBalance, withdrawalBalance.negate());
&#125;

public ActivityWindow(@NonNull List<Activity> activities) &#123;
this.activities = activities;
&#125;

public ActivityWindow(@NonNull Activity... activities) &#123;
this.activities = new ArrayList<>(Arrays.asList(activities));
&#125;

public List<Activity> getActivities() &#123;
return Collections.unmodifiableList(this.activities);
&#125;

public void addActivity(Activity activity) &#123;
this.activities.add(activity);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Account类定义了calculateBalance、withdraw、deposit方法；ActivityWindow类定义了calculateBalance方法</p>
</blockquote>
<h2 data-id="heading-7">小结</h2>
<p>buckpal工程adapter、application、domain三层；其中application层定义了port包，该包定义了in、out两种类型的接口；adapter层也分in、out两类，分别实现application/port层的接口；application的service则实现了port的接口。其中domain层不依赖任何层；application层的port定义了接口，然后service层实现接口和引用接口；adapter层则实现了application的port层的接口。</p>
<h2 data-id="heading-8">doc</h2>
<ul>
<li><a href="https://github.com/thombergs/buckpal/" target="_blank" rel="nofollow noopener noreferrer">buckpal</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            