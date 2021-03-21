
---
title: 聊聊buckpal对于Hexagonal Architecture的实践
categories: 
    - 编程
    - 掘金 - 标签
author: 掘金 - 标签
comments: false
date: Sat, 20 Mar 2021 06:17:59 GMT
thumbnail: 
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><h2 data-id="heading-0">序</h2>
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
<pre><code class="copyable">public interface GetAccountBalanceQuery {

Money getAccountBalance(AccountId accountId);

}

@Value
@EqualsAndHashCode(callSuper = false)
public
class SendMoneyCommand extends SelfValidating<SendMoneyCommand> {

    @NotNull
    private final AccountId sourceAccountId;

    @NotNull
    private final AccountId targetAccountId;

    @NotNull
    private final Money money;

    public SendMoneyCommand(
            AccountId sourceAccountId,
            AccountId targetAccountId,
            Money money) {
        this.sourceAccountId = sourceAccountId;
        this.targetAccountId = targetAccountId;
        this.money = money;
        this.validateSelf();
    }
}

public interface SendMoneyUseCase {

boolean sendMoney(SendMoneyCommand command);

}
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>application/port/in定义了GetAccountBalanceQuery、SendMoneyUseCase接口</p>
</blockquote>
<h3 data-id="heading-4">out</h3>
<pre><code class="copyable">public interface AccountLock {

void lockAccount(Account.AccountId accountId);

void releaseAccount(Account.AccountId accountId);

}

public interface LoadAccountPort {

Account loadAccount(AccountId accountId, LocalDateTime baselineDate);
}

public interface UpdateAccountStatePort {

void updateActivities(Account account);

}
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>application/port/out定义了AccountLock、LoadAccountPort、UpdateAccountStatePort接口</p>
</blockquote>
<h2 data-id="heading-5">application/service</h2>
<pre><code class="copyable">@RequiredArgsConstructor
class GetAccountBalanceService implements GetAccountBalanceQuery {

private final LoadAccountPort loadAccountPort;

@Override
public Money getAccountBalance(AccountId accountId) {
return loadAccountPort.loadAccount(accountId, LocalDateTime.now())
.calculateBalance();
}
}

@Component
class NoOpAccountLock implements AccountLock {

@Override
public void lockAccount(AccountId accountId) {
// do nothing
}

@Override
public void releaseAccount(AccountId accountId) {
// do nothing
}

}

@RequiredArgsConstructor
@UseCase
@Transactional
public class SendMoneyService implements SendMoneyUseCase {

private final LoadAccountPort loadAccountPort;
private final AccountLock accountLock;
private final UpdateAccountStatePort updateAccountStatePort;
private final MoneyTransferProperties moneyTransferProperties;

@Override
public boolean sendMoney(SendMoneyCommand command) {

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
if (!sourceAccount.withdraw(command.getMoney(), targetAccountId)) {
accountLock.releaseAccount(sourceAccountId);
return false;
}

accountLock.lockAccount(targetAccountId);
if (!targetAccount.deposit(command.getMoney(), sourceAccountId)) {
accountLock.releaseAccount(sourceAccountId);
accountLock.releaseAccount(targetAccountId);
return false;
}

updateAccountStatePort.updateActivities(sourceAccount);
updateAccountStatePort.updateActivities(targetAccount);

accountLock.releaseAccount(sourceAccountId);
accountLock.releaseAccount(targetAccountId);
return true;
}

private void checkThreshold(SendMoneyCommand command) {
if(command.getMoney().isGreaterThan(moneyTransferProperties.getMaximumTransferThreshold())){
throw new ThresholdExceededException(moneyTransferProperties.getMaximumTransferThreshold(), command.getMoney());
}
}

}
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>application/service的GetAccountBalanceService实现了application.port.in.GetAccountBalanceQuery接口；NoOpAccountLock实现了application.port.out.AccountLock接口；SendMoneyService实现了application.port.in.SendMoneyUseCase接口</p>
</blockquote>
<h2 data-id="heading-6">domain</h2>
<pre><code class="copyable">@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class Account {

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
 * Creates an {@link Account} entity without an ID. Use to create a new entity that is not yet
 * persisted.
 */
public static Account withoutId(
Money baselineBalance,
ActivityWindow activityWindow) {
return new Account(null, baselineBalance, activityWindow);
}

/**
 * Creates an {@link Account} entity with an ID. Use to reconstitute a persisted entity.
 */
public static Account withId(
AccountId accountId,
Money baselineBalance,
ActivityWindow activityWindow) {
return new Account(accountId, baselineBalance, activityWindow);
}

public Optional<AccountId> getId(){
return Optional.ofNullable(this.id);
}

/**
 * Calculates the total balance of the account by adding the activity values to the baseline balance.
 */
public Money calculateBalance() {
return Money.add(
this.baselineBalance,
this.activityWindow.calculateBalance(this.id));
}

/**
 * Tries to withdraw a certain amount of money from this account.
 * If successful, creates a new activity with a negative value.
 * @return true if the withdrawal was successful, false if not.
 */
public boolean withdraw(Money money, AccountId targetAccountId) {

if (!mayWithdraw(money)) {
return false;
}

Activity withdrawal = new Activity(
this.id,
this.id,
targetAccountId,
LocalDateTime.now(),
money);
this.activityWindow.addActivity(withdrawal);
return true;
}

private boolean mayWithdraw(Money money) {
return Money.add(
this.calculateBalance(),
money.negate())
.isPositiveOrZero();
}

/**
 * Tries to deposit a certain amount of money to this account.
 * If sucessful, creates a new activity with a positive value.
 * @return true if the deposit was successful, false if not.
 */
public boolean deposit(Money money, AccountId sourceAccountId) {
Activity deposit = new Activity(
this.id,
sourceAccountId,
this.id,
LocalDateTime.now(),
money);
this.activityWindow.addActivity(deposit);
return true;
}

@Value
public static class AccountId {
private Long value;
}

}

public class ActivityWindow {

/**
 * The list of account activities within this window.
 */
private List<Activity> activities;

/**
 * The timestamp of the first activity within this window.
 */
public LocalDateTime getStartTimestamp() {
return activities.stream()
.min(Comparator.comparing(Activity::getTimestamp))
.orElseThrow(IllegalStateException::new)
.getTimestamp();
}

/**
 * The timestamp of the last activity within this window.
 * @return
 */
public LocalDateTime getEndTimestamp() {
return activities.stream()
.max(Comparator.comparing(Activity::getTimestamp))
.orElseThrow(IllegalStateException::new)
.getTimestamp();
}

/**
 * Calculates the balance by summing up the values of all activities within this window.
 */
public Money calculateBalance(AccountId accountId) {
Money depositBalance = activities.stream()
.filter(a -> a.getTargetAccountId().equals(accountId))
.map(Activity::getMoney)
.reduce(Money.ZERO, Money::add);

Money withdrawalBalance = activities.stream()
.filter(a -> a.getSourceAccountId().equals(accountId))
.map(Activity::getMoney)
.reduce(Money.ZERO, Money::add);

return Money.add(depositBalance, withdrawalBalance.negate());
}

public ActivityWindow(@NonNull List<Activity> activities) {
this.activities = activities;
}

public ActivityWindow(@NonNull Activity... activities) {
this.activities = new ArrayList<>(Arrays.asList(activities));
}

public List<Activity> getActivities() {
return Collections.unmodifiableList(this.activities);
}

public void addActivity(Activity activity) {
this.activities.add(activity);
}
}
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
            