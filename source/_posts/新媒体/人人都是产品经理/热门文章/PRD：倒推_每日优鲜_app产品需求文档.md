
---
title: 'PRD：倒推_每日优鲜_app产品需求文档'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/oyc0eau0XMeJgx4xeF3Z.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 14 Mar 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/oyc0eau0XMeJgx4xeF3Z.jpg'
---

<div>   
<blockquote><p>疫情过后，线上买菜会成为趋势吗？每日优鲜作为一个比较成熟的O2O生鲜电商平台，我根据现有的每日优鲜app进行了文档倒推，对产品结构、主要业务流程、主要窗口的页面逻辑和交互进行了简要的分析和说明。</p>
<p>该文档主要是从前端用户体验方面设计的，刚开始学习相关知识，肯定有很多不足，还请各位大佬多多指正！鞠躬~</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-3517627" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/oyc0eau0XMeJgx4xeF3Z.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>版本修订历史：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/QNo5BS9r8jdJ9vD5KztW.png" alt width="839" height="135" referrerpolicy="no-referrer"></p>
<p>PRD输出环境：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/6uwtLh4OK7zYoZa7trL1.png" alt width="414" height="144" referrerpolicy="no-referrer"></p>
<p>图标：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/vvRLfjd6IVPQwIZmQCEz.png" alt width="150" height="150" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">目录</h2>
<blockquote><p>一、产品概述</p>
<p>1.1产品背景介绍</p>
<p>1.2产品概述</p>
<p>1.3产品定位</p>
<p>1.4目标用户</p>
<p>二、产品结构及业务流程</p>
<p>2.1产品功能结构图</p>
<p>2.2产品信息结构图</p>
<p>2.3业务流程图——用户购买功能</p>
<p>三、全局说明</p>
<p>3.1功能权限</p>
<p>3.2键盘说明</p>
<p>3.3页面内交互</p>
<p>四、页面功能详细说明</p>
<p>4.1登录页</p>
<p>4.2首页</p>
<p>4.3商品详情页</p>
<p>4.4分类页面</p>
<p>4.6我的页面</p>
<p>4.7吃什么页面</p>
<p>五、总结</p></blockquote>
<h2 id="toc-2">一、产品概述</h2>
<h3>1.1 产品背景介绍</h3>
<p>互联网的发展、年轻消费者消费习惯的改变、冷链物流技术的不断进步，加之新零售的机遇，我国生鲜电商行业保持了较快的发展速度。</p>
<p>消费者生鲜消费习惯改变：CBNData《2017中国家庭餐桌消费潮流报告》：线上品牌生鲜销售额占比从2014年的6%上升至60.5%。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/TIkPIu5cLYDOoGDhkpzE.png" alt width="288" height="226" referrerpolicy="no-referrer"></p>
<p>精选生鲜需求上升：进口优质生鲜市场份额上升。</p>
<p>做B2C生鲜移动电商有利可图！</p>
<h3>1.2 产品概述</h3>
<p>每日优鲜是一个围绕着老百姓餐桌的生鲜O2O电商平台。覆盖了水果、蔬菜、肉蛋、水产、零食、乳品、轻食、粮油、酒饮、速食、轻食、日百等20个品类的布局，并在全国 20 多个主要城市建立起“城市分选中心＋社区前置仓”的极速达冷链物流体系，为用户提供自营精选生鲜最快1小时送达服务。</p>
<h3>1.3 产品定位</h3>
<p>全品类精选商品+1小时极速达物流+社交化会员制运营。</p>
<h3>1.4 目标用户</h3>
<ul>
<li>女性</li>
<li>18-35岁的年轻人：工作繁忙+刚成立家庭+喜好网购+重视时间效率；</li>
<li>一二线城市+东部沿海地区：经济条件好+工作竞争强烈+空闲时间较少；</li>
<li>白领、大学生、宝妈、特殊情况不能出门采购的用户。</li>
</ul>
<h2 id="toc-3">二、产品结构及业务流程</h2>
<h3>2.1 产品功能结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/VItAkkHuga5WspawoKYm.png" alt width="952" height="1142" referrerpolicy="no-referrer"></p>
<h3>2.2 产品信息结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/smXSgGvuS5DujJg3kLqR.png" alt width="959" height="1016" referrerpolicy="no-referrer"></p>
<h3>2.3 业务流程图——用户购买功能</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/etGGbHQVIXN0L1JVPK3y.png" alt width="565" height="746" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">三、全局说明</h2>
<h3>3.1 功能权限</h3>
<p><strong>（1）是否登陆</strong></p>
<ul>
<li>登录状态可进行APP内所有操作</li>
<li>非登录状态下：无法订单结算；无法进入消息、邀请有礼以及好友助力提现等活动页面、“吃什么”社区页面</li>
</ul>
<p><strong>（2）是否会员</strong></p>
<ul>
<li>普通用户：没有会员权益，其余功能均可用</li>
<li>优享会员：商品享有会员价、可以参与超级会员日活动、积分加倍、可以分享给好友会员体验卡、拥有专属客服</li>
</ul>
<h3>3.2 键盘说明</h3>
<p>（1）登陆页面中点击手机号输入框，页面底部弹出数字键盘；</p>
<p>（2）首页、分类、社区页面点击搜索框是页面底部弹出字母全键盘；</p>
<p>（3）在评价页面点击评价框时弹出字母全键盘。</p>
<h3>3.3 页面内交互</h3>
<p>toast、actionbar、dialog这三种形式在后文均有提到，这里就不在对这三种常见的反馈形式做过多的赘述。</p>
<p>页面异常如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/OAfBxTkCIFCGA1a3HdKW.png" alt width="1056" height="659" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">四、页面功能详细说明</h2>
<p>每日优鲜底部标签栏有5个标签，分别是：首页、分类、吃什么、购物车、我的。接下来我将围绕这五个标签页详细阐述具体的页面功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/CHRdNM9hyMlYoHKH5Ugt.gif" alt width="228" height="446" referrerpolicy="no-referrer"></p>
<h3>4.1 登录页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/6NxTrGwuXcqYl0IVJIxp.png" alt width="1339" height="838" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>输入手机号、获取验证码、第三方登录入口。</p>
<p><strong>用户场景：</strong></p>
<ul>
<li>用户第一次使用，用户登录新的账号以及使用新的设备登录，或老用户退出后再次登陆。</li>
<li>游客用户执行购买、个人消息、参加优惠活动等需要登陆的操作。</li>
</ul>
<p><strong>优先级：</strong>高。</p>
<p><strong>前置条件：</strong>打开每日优鲜后选择我的标签页，即可看到登录选项，或点击任意一个游客身份功能受限键则可以跳转到该页面。</p>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>用户输入手机号码，点击“获取验证码”按钮；</li>
<li>若用户在60秒内未收到手机验证码，点击“获取验证码”按钮重新获取验证码；</li>
<li>用户也可以点击总登录注册页面底部其他登录方式的微信登陆按钮进行授权登录；</li>
<li>勾选“同意用户使用协议和隐私政策”才能点击“登陆”或“微信登陆”。</li>
</ul>
<p><strong>后置条件：</strong>登录成功/重新获取验证码登录。</p>
<p><strong>页面交互：</strong></p>
<ul>
<li>手机号默认+86，输入限制11位，当输入大于11位数字时，弹出Toast提示“您输入的手机号超过了11位”提示文本；</li>
<li>点击手机号、验证码输入框时，数字键盘从底部向上弹出；</li>
<li>获取验证码后，按钮内容变为“60S后重发”并降低灰度开始60秒倒数，60S后按钮内容变回原本内容；</li>
<li>用户点击第三方登陆下的三个按钮，相应的第三方授权页面从页面右侧弹出。</li>
</ul>
<p><strong>异常流程：</strong>用户输入短信验证码错误，弹出Toast提示“验证码错误，请确认后再次尝试”提示文本，3秒后消失，用户重新操作。</p>
<h3>4.2 首页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/yiuvtR4Obe97rnKWbvNy.gif" alt width="229" height="450" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/46sXdMZElrdryrtZD0g8.png" alt width="567" height="444" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>展示商品和活动信息、对商品分类、推荐商品信息。</p>
<p><strong>优先级：</strong>高</p>
<p><strong>前置条件：</strong>打开每日优鲜APP后首先显示的内容或点击底部导航栏中的“首页”功能标签。</p>
<p><strong>页面结构：</strong></p>
<ol>
<li>用户位置定位；</li>
<li>商品搜索框；</li>
<li>活动/广告banner页，6例活动/广告页轮播；</li>
<li>商品分类tab导航，共10类；</li>
<li>活动标签区；</li>
<li>热销商品推荐区；</li>
<li>商品专题活动区；</li>
<li>特色商品分类栏专题区，共7类。</li>
</ol>
<p><strong>刷新机制：</strong></p>
<ul>
<li>下拉页面进行刷新；</li>
<li>进入此页面自动刷新。</li>
</ul>
<p><strong>逻辑内容详细说明：</strong></p>
<h3>1. 用户位置定位</h3>
<p>系统默认显示上一次用户选择的地址，点击后页面跳转至选择其他收货地址页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/11S5QvWNZYbgpwU9dfTX.gif" alt width="239" height="469" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>选择、添加、更改收货地址。</p>
<p><strong>用户场景：</strong>用户想要更改收货地址、选择其他已添加的收货地址、新增收货地址。</p>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>在选择其他收货地址页面，用户点击输入框输入新收货地址，会自动显示与包含输入地址字符的所有地址选项，选择好后页面自动转回至首页，用户收货地址变更为已输入的地址。</li>
<li>其他收货地址页面结构分为城市选择框、文本搜索框、当前定位、用户已存储的收货地址、附近地址共5部分内容。</li>
<li>用户选择城市后，在文本搜索框内输入具体地址内容进行搜索（支持内容模糊搜索），在下拉备选列表中给出相关搜索内容的具体地址及距离公里数。</li>
<li>系统对已搜索过的内容自动标签化添加到历史记录中（历史搜索规则描述：按搜索的时间倒序排列，排列方式从上至下排列，可点击垃圾桶图标清除所有历史搜索内容）。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>在“首页”点击送货地址，选择收货地址页面从右侧弹出。</li>
<li>在“选择收货地址”页面下点击“请输入您的收货地址”文本框，字母键盘从底部弹出，文本框在输入文本后，原文本框提示内容消失，出现下拉备选列表，列表里显示与搜索内容相关的地址，点击“取消”回到“选择收货地址”页面。</li>
<li>在“选择收货地址”页面点击“新增地址”，新增收货地址页面从右侧弹出，点击手机号输入框，数字键盘从页面底部弹出；点击“+通讯录”，页面中间跳出dialog弹窗，请求访问用户通讯录，用户选择“好”，从底部弹出通讯录页面，用户选择“取消”，回到当前页面；点击“收货地址”文本框，地址搜索页面从右侧弹出；点击门牌号输入框，字母全键盘从页面底部弹出。</li>
<li>在选择当前定位、已存储的收货地址、附近地址栏目中的地址后，收货地址页面从右侧滑出，跳转回首页。</li>
</ul>
<p>思考改进：用户在文本搜索框内输入具体地址内容进行搜索时，在下拉备选列表中的文本与输入框中搜索内容相关的文本可以被加粗显示。</p>
<h3>2. 商品搜索框</h3>
<p>用户可以直接点击搜索框后，页面跳转至搜索框hint的商品信息界面，也可自己输入想购买商品的关键字进行特定搜索。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/MOBmBvISUfITtWycT8dy.gif" alt width="245" height="481" referrerpolicy="no-referrer"></p>
<p><strong>功能：</strong>搜索商品。</p>
<p><strong>用户场景：</strong>用户需要快速获得想要购买的商品的信息。</p>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>搜索页面结构分为搜索框、搜索历史、热门热搜三部分。</li>
<li>用户在搜索框内输入商品进行搜索，支持内容模糊搜索，搜索完成后页面转至包含搜索词的相应的商品搜索结果页面，没有库存的商品显示“已抢光”，不能添加购物车，但可以寻找相似商品。</li>
<li>系统对已搜索过的内容自动标签化添加到历史搜索内容点击“垃圾桶”按钮可删除搜索历史。</li>
<li>“搜索历史”规则描述：按搜索的时间倒叙排列，排列方式从左至右、从上至下排列，可两排展示10条历史搜索内容，字数长度限制为10字符，超出部分用“…”代替。</li>
<li>热门搜索内容是系统根据定位，为用户推荐附近多数用户搜索的榜单商品，按搜索热度百分比降序排列，点击相应标签，进入相应商品推荐页面，最多可展示15条热门搜索内容，并将热门搜索前三商品加粗显示。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>在“首页”页面点击搜索框，搜索页面从右侧弹出，同时字母全键盘从页面底部弹出。</li>
<li>搜索框内会自动显示推荐商品名，输入文本后，默认推荐内容消失，当前页面其他内容隐藏，同时弹出下拉备选列表，系统会根据输入的汉字提供相关的搜索关键词，在下拉备选列表中的文本与输入框中搜索内容相关的文本被加粗显示。</li>
<li>点击搜索历史右侧的“垃圾桶”按钮可清除所有历史搜索内容。</li>
<li>通过搜索框搜索商品、点击搜索历史标签、热门搜索标签，商品搜索结果页面直接弹出。</li>
</ul>
<h3>3. 活动/广告banner页</h3>
<p><strong>页面逻辑：</strong>6例活动/广告页轮播，点击可转到相关活动/广告页面。</p>
<p><strong>页面交互：</strong>点击活动/广告Banner区域，活动/广告页面从右侧弹出。</p>
<h3>4. 商品分类tab导航</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/wKZVgtyuBfsjiCLgvdaD.png" alt width="536" height="474" referrerpolicy="no-referrer"></p>
<p><strong>用户场景：</strong>用户知道自己想要购买商品的类别，想要在某一特定类别内挑选商品。</p>
<p><strong>页面逻辑：</strong>商品分类标签区共十类，点击相应的标签可进入“分类”页面，同时出现相关商品推荐页面。</p>
<p><strong>页面交互：</strong>点击“首页”页面中的商品分类标签会迅速跳转至“分类”页面，同时显示出tab对应的商品列表。</p>
<h3>5. 活动标签区</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/8ZnOKuNRy7KsNW0Vjuxg.png" alt width="460" height="417" referrerpolicy="no-referrer"></p>
<p><strong>用户场景：</strong>价格敏感型用户或者忠实用户想要通过各种活动优惠来节省一笔开支。</p>
<p><strong>页面逻辑：</strong>活动标签区共四类，点击相应的标签可进入相应的活动页面。</p>
<p><strong>页面交互：</strong>点击“首页”页面中的活动标签，相应的活动页面会从右侧弹出。</p>
<h3>6. 热销商品推荐区</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/XZY252OUoHLj9vn05y8x.png" alt width="595" height="439" referrerpolicy="no-referrer"></p>
<p><strong>用户场景：</strong>用户不知道购买哪种商品，从众心理会驱使用户浏览热销商品。</p>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>热销商品排行榜为用户推荐附近多数用户购买的商品，按销量百分比降序排列，点击相应标签，可以进入相应商品的详情页面，或直接点击加号，将商品加入购物车中。</li>
<li>点击查看更多直接跳转至热销排行榜页面。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>热销排行榜商品列表可横向滑动显示12个商品，滑到最右边出现“查看更多”，继续向左滑动，“热销排行榜”页面就会从右侧弹出。</li>
<li>点击“查看更多”按钮，“热销排行榜”页面也从右侧弹出。</li>
<li>点击热销排行榜横向滑动商品列表中的商品，对应的商品详情页会从右侧弹出。</li>
<li>直接点击加号添加购物车，有1s的“商品放入购物车”的动画。</li>
</ul>
<h3>7. 商品专题活动区</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/N0kpuCBzkWCfJq9garfD.png" alt width="567" height="432" referrerpolicy="no-referrer"></p>
<p><strong>用户场景：</strong>用户想要购买打折或有优惠价格的活动商品。</p>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>专题活动标签区共六类，点击相应的标签可进入相应的活动页面。</li>
<li>这里以“每日秒杀”活动页面为例进行介绍，“每日秒杀”活动页面，分为标题栏、结束倒计时栏和活动商品列表三部分，点击商品列表中的商品区域可进入相应商品的详情页面。</li>
<li>活动商品列表中的商品介绍会显示商品的库存和已抢购人数。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>“首页”页面中的活动标签，相应的活动页面会从右侧弹出。</li>
<li>点击“每日秒杀”活动页面商品列表中的商品区域右侧会弹出相应商品的详情页面。</li>
<li>点击“每日秒杀”活动页面左下角的购物车按钮，购物车页面从右侧弹出。</li>
<li>点击“马上抢”按钮，商品将被自动加入购物车中，同时页面左下方购物车上的数字加1。</li>
</ul>
<h3>8. 特色商品分类栏专题区</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/Vk1P9CDXevp6HZgS168N.gif" alt width="232" height="454" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/W1m2gM6BYH4tfWbwwiuu.png" alt width="492" height="463" referrerpolicy="no-referrer"></p>
<p><strong>用户场景:</strong></p>
<ul>
<li>用户打开APP进入首页，想直接在首页挑选相应类别的商品。</li>
<li>用户想购买商品，但不知道具体购买什么，可以通过浏览此页面进行挑选。</li>
</ul>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>系统为用户推荐了一些用户可能喜欢的商品，用户可全部查看、也可点击不同的分类标签（如鲜鱼鲜肉、在家火锅、一件包邮等）查看相关商品推荐列表。</li>
<li>在商品推荐列表中点击商品可进入相应的商品详情页面，也可直接把商品加入购物车。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>下滑“首页”页面，用户可以左右滑动横排标签栏，默认选中标签为“全部”。</li>
<li>当点击标签区的各个标签时，功能标签呈现选中状态；同时，页面下方弹出相应类别的商品推荐列表。</li>
<li>点击横排标签滑动区的7个标签中第3、4、5个标签，标签行会自动向左或向右滑动。</li>
<li>特色商品分类栏专题区可向下滑动浏览相应标签下的更多商品。</li>
<li>点击下方商品推荐列表中的商品区域，商品详情页从右侧弹出。</li>
<li>点击商品旁的加号，会有1s的商品放入底部标签栏的购物车的动画。</li>
</ul>
<p><strong>对首页整体的思考：</strong>“每日优鲜”APP用商品搜索框、广告banner、商品分类tab导航、热销商品推荐区、专题活动区、特色商品推荐区这六大模块，对不同用户的不同需求提供相应的引导方案，这六个用户需求入口集中到同一出口“商品详情页”，驱使用户加入购物车。每日优鲜可以根据用户的浏览、搜索和订单记录更精准地向用户推荐商品。</p>
<h3>4.3 商品详情页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/2IlSYFTyLo5AowpL1FSz.gif" alt width="257" height="504" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/lI4GqMRb2ccEl4gdD41B.png" alt width="580" height="436" referrerpolicy="no-referrer"></p>
<p><strong>页面结构：</strong></p>
<ol>
<li>商品图片</li>
<li>商品简介</li>
<li>商品所在榜单</li>
<li>活动分享</li>
<li>推荐商品</li>
<li>菜谱做法</li>
<li>商品详情</li>
</ol>
<p><strong>功能描述：</strong>用户在商品详情页面可查看商品的具体信息并加入购物车，还可以分享商品到微信和朋友圈。</p>
<p><strong>前置条件：</strong>点击所有页面中的具体商品。</p>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>在商品详情页面包含五张商品的图片；</li>
<li>点击商品图片右上角“分享”按钮，可以选择微信或朋友圈进行分享；</li>
<li>点击榜单可进入“热销排行榜界面”，并显示该商品所在的榜单类别里的所有商品；</li>
<li>点击分享可进入“天天赚钱”活动界面；</li>
<li>在相关推荐商品列表中点击商品可进入相关商品详情页面，点击加号可以直接加入购物车；</li>
<li>点击“加入购物车”按钮可直接将商品加入购物车；</li>
<li>菜谱做法区包含相关菜品的菜谱信息，点击菜谱可进入相应的菜谱详情页面。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>在商品的图片上左右滑动，可查看商品的不同图片；</li>
<li>点击图片左上方的“返回”按钮可返回之前的页面；</li>
<li>在商品详情页面向下拖动可查看商品详情等其他信息；</li>
<li>点击“分享”按钮，商品详情页面变暗产生遮罩层，同时分享页面从底部弹出，点击分享路径图标可分享至相关途径，点击“取消”按钮或点击外，返回到原来的商品详情页；</li>
<li>点击“加入购物车”选项，右上角购物车角标数字加1，同时会有1s的商品放入购物车的动画；</li>
<li>点击页面左下角的“购物车”图标，购物车页面从右侧弹出；</li>
<li>滑动菜谱列表可查看菜谱信息，点击菜谱列表中的菜谱，相应的菜谱详情页面从右侧弹出。</li>
</ul>
<h3>4.4 分类页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/qY8CoNQLm783K7lPcciC.png" alt width="395" height="483" referrerpolicy="no-referrer"></p>
<p><strong>页面结构：</strong></p>
<ol>
<li>搜索框；</li>
<li>商品分类tab导航（主标签），共11类；</li>
<li>商品细分类别导航（子标签），不同商品大类的细分类别不同；</li>
<li>广告banner；</li>
<li>具体商品列表。</li>
</ol>
<p><strong>功能描述：</strong>选择商品的分类标签，可进入相应的商品推荐页面。</p>
<p><strong>用户场景：</strong></p>
<ul>
<li>用户想要通过商品分类挑选商品；</li>
<li>用户想参考商品的销量来选择商品；</li>
<li>价格敏感的用户需要对商品进行价格排序，从而挑选出低价商品。</li>
</ul>
<p><strong>优先级：</strong>高</p>
<p><strong>前置条件：</strong>点击页面底部导航栏的“分类“标签。</p>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>点击搜索框，进入商品搜索页面；</li>
<li>点击广告banner区的广告进入相应的广告界面；</li>
<li>点击商品分类tab导航的标签页面右侧出现相应的商品大类的推荐页面；</li>
<li>点击左侧商品细分类别导航的标签页面右侧出现相应细分类类别的推荐页面；</li>
<li>商品可以按综合、销量、价格进行排序显示；</li>
<li>点击商品直接进入商品详情界面，或点击加号，可将商品直接加入购物车。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>在“分类”页面上方点击搜索框，商品搜索页面从右侧弹出，同时字母键盘从页面底部弹出；</li>
<li>点击广告活动banner区的广告，相应的广告界面从右侧弹出；</li>
<li>主标签可以左右滑动，子标签可以上下滑动，查看更多信息；</li>
<li>选中标签的内容时，字体会加粗显示；</li>
<li>点击商品分类页面中的主标签，相应的商品推荐页面和商品子标签从页面下半部分加载出来；</li>
<li>在商品推荐页面上方点击综合、销量、价格等排序按钮，商品推荐页面会自动更新，重新加载；</li>
<li>点击每个商品右方的加号图标，商品旁的数字+1，同时数字左边出现“－”按钮，底部导航页的购物车右角标数字+1，同时会有1s的商品放入购物车的动画。</li>
</ul>
<h3>4.5 购物车页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/U5ip4uMYweHky97eIMfy.png" alt width="613" height="670" referrerpolicy="no-referrer"></p>
<p><strong>页面结构：</strong></p>
<ol>
<li>用户位置定位；</li>
<li>购物车商品列表；</li>
<li>猜你喜欢商品推荐区；</li>
<li>结算区。</li>
</ol>
<p><strong>功能描述：</strong>选择想要购买的商品，点击结算按钮即可下单支付。</p>
<p><strong>用户场景：</strong>用户想要挑选商品进行结算。</p>
<p><strong>优先级：</strong>高</p>
<p><strong>前置条件：</strong></p>
<ul>
<li>点击页面底部导航栏的“购物车“标签；</li>
<li>点击商品详情页左下角购物车icon；</li>
<li>点击菜谱详情页右上角购物车icon；</li>
<li>点击广告活动详情页购物车浮标。</li>
</ul>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>在购物车页面下，用户可以查看添加到购物车的商品，也可点击查看商品详情；</li>
<li>用户可以改变购物车内商品的数量，也可以同时选择对一种或多种商品进行结算或删除；</li>
<li>用户点击去结算按钮进入结算页面可以更改收货地址、选择送达时间、选择优惠红包和选择支付方式，极速达商品默认送达时间为接下来一小时；</li>
<li>结算页面有商品合计价格、活动优惠以及运费的信息；</li>
<li>在结算页面未支付返回购物车会出现dialog弹窗提示用户是否要离开。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>用户点击页面上方定位Icon，选择售后地址页面从右侧弹出；</li>
<li>点击勾选商品或全选的“白色圆圈”，圆圈上会显示玫红色的勾，页面右下方合计价格通过单价*数量算出并显示在去结算按钮左边，“去结算”按钮填充玫红色；</li>
<li>用户点击商品，相应的商品详情页面从右侧弹出；</li>
<li>用户点击商品订单中的“+” “-”按钮，可改变结算商品的数量；若商品数量为1，点击商品订单中的“-”按钮，页面中间出现dialog弹窗，询问顾客是否删除该商品；</li>
<li>点击填充玫红色的“去结算”按钮，填写订单（支付）页面从右侧弹出；</li>
<li>用户点击猜你喜欢区域商品旁的加号，底部导航页的购物车右角标数字+1，这时没有动画；</li>
<li>用户点击商品旁的“可用优惠券”按钮，相应的优惠券Actionbar向上滑动显示，点击弹窗右上角的X或遮罩，“优惠券”弹窗向下滑出，同时遮罩消失。</li>
</ul>
<h3>4.6 我的页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/1n7EMMsuBFbKj5iou0HZ.gif" alt width="238" height="466" referrerpolicy="no-referrer"></p>
<p><strong>页面结构：</strong></p>
<ol>
<li>用户信息（头像、用户名、账户信息）；</li>
<li>消息提醒；</li>
<li>订单信息；</li>
<li>广告活动；</li>
<li>用户服务栏。</li>
</ol>
<p><strong>功能描述：</strong>查看订单状态、活动消息提醒、兑换积分、联系客服、参加优惠活动、更改账户信息。</p>
<p><strong>用户场景：</strong></p>
<ul>
<li>用户想要更改账号信息；</li>
<li>用户想要充值；</li>
<li>用户想要把积分兑换成商品；</li>
<li>用户想查看订单状态；</li>
<li>用户想联系客服寻求帮助；</li>
<li>用户想退出登录；</li>
<li>用户想开发票。</li>
</ul>
<p><strong>优先级：</strong>高。</p>
<p><strong>前置条件：</strong>点击页面底部导航栏的“我的”标签。</p>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>点击页面左上角铃铛icon出现消息页面，提示用户相关的优惠活动；</li>
<li>点击积分兑换、积分商城出现福利社页面，可供用户兑换商品；</li>
<li>点击我的订单部分的标签栏可查看订单状态、评价订单和订单售后；</li>
<li>点击“全部订单”可查看用户的所有订单，并提供开发票服务；</li>
<li>点击活动标签可进入相关活动详情页；</li>
<li>点击货地址可新增和更改现有收货地址；</li>
<li>点击客服可进入客服与帮助界面；</li>
<li>点击设置可退出登陆和查看app相关信息。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>点击页面左上角铃铛icon，活动消息页面从右侧弹出；</li>
<li>点击“立即开通”按钮，开通会员的“优享会员专场”页面从右侧弹出；</li>
<li>点击“全部订单”用户的所有订单页面从右侧弹出；</li>
<li>点击我的订单区域相应标签（待支付、待配送、配送中、待评价、售后），相应页面从右侧弹出；</li>
<li>点击活动标签，相关活动详情页从右侧弹出；</li>
<li>点击货地址，我的收货地址页面从右侧弹出；</li>
<li>点击客服，客服与帮助界面从右侧弹出；</li>
<li>点击设置，设置页面从右侧弹出。</li>
</ul>
<h3><strong>4.7 吃什么页面</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/43u6GMOlKDVBMWhmFBiK.gif" alt width="240" height="470" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/DihwGkxthHlowv409Hqy.png" alt width="367" height="498" referrerpolicy="no-referrer"></p>
<p><strong>页面结构：</strong></p>
<ol>
<li>菜谱、食材搜索框；</li>
<li>PGC专栏；</li>
<li>UGC专栏，横向列表分为8类，点击右侧列表图标可展开更多；</li>
<li>用户头像。</li>
</ol>
<p><strong>功能描述：</strong>查看菜谱分类、查看菜谱的图文和视频信息、查看或加购菜谱里的链接商品、查查看用户主页、点赞、收藏、分享。</p>
<p><strong>用户场景：</strong></p>
<ul>
<li>用户买了商品不知如何制作，想要搜索商品的菜谱；</li>
<li>用户想分享自己的厨艺，获得自我实现和满足感；</li>
<li>用户不知道吃什么，想看看他人分享的菜谱寻找灵感；</li>
<li>用户想提升自己的厨艺，需要学习一些菜谱。</li>
</ul>
<p><strong>优先级：</strong>高</p>
<p><strong>前置条件：</strong></p>
<ul>
<li>点击页面底部导航栏的“吃什么“标签；</li>
<li>在商品详情页菜谱做法区点击任一菜谱区域。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/03/09YAtPQWkX9QMQOvU6JH.png" alt width="695" height="969" referrerpolicy="no-referrer"></p>
<p><strong>页面逻辑：</strong></p>
<ul>
<li>点击搜索框，进入菜谱搜索页面；</li>
<li>点击头像进入用户个人中心；</li>
<li>点击暖心推荐下方图片进入相关的内容页面；</li>
<li>点击下方菜谱分类别导航的标签页面下方出现相应类别的推荐菜谱；</li>
<li>点击商品分类tab右侧的列表icon，会展开更详细的类别供挑选；</li>
<li>在今日推荐板块，用户可以对喜欢的菜谱进行点赞操作，点赞后会把相应菜谱加入到个人中心页面的点赞区域；</li>
<li>点击具体的菜谱会直接进入菜谱详情界面，下拉会出现食材清单区域，点击相应食材旁的加号，可将商品直接加入购物车，点击相应食材的图片/视频，会跳转商品详情页；</li>
<li>在菜谱详情界面，可以对菜谱进行点赞、收藏、分享操作；点赞、收藏后会把相应菜谱加入到个人中心页面的点赞、收藏区域。</li>
</ul>
<p><strong>页面交互：</strong></p>
<ul>
<li>上下滑动浏览内容；</li>
<li>点击搜索框，搜索页面从右侧弹出，同时字母全键盘从页面底部弹出；</li>
<li>点击用户头像，用户详情页从右侧弹出；</li>
<li>点击暖心推荐“优鲜小厨”发布的官方内容，相应内容界面从右侧弹出；</li>
<li>点击菜谱图片或视频，菜谱详情页从右侧弹出；</li>
<li>点击❤图标给用户点赞，灰色的❤会变成玫红色，再点击一下玫红色的❤会重新变为灰色。</li>
</ul>
<p><strong>页面整体思考和建议：</strong></p>
<ol>
<li>“吃什么”页面为用户提供了社区，增强了用户黏性。</li>
<li>帮助购买了菜品不知如何制作的用户提供了方便的制作方法。</li>
<li>以前往往是用户想做什么菜，然后在去搜索相应食材，就会比较麻烦。现在用户可以直接搜索出菜谱，在菜谱详情页的食材清单中，把食材直接加入购物车。</li>
<li>搜索框暂不支持内容模糊搜索，不会弹出备选列表。</li>
<li>菜谱图文详情页页面顶端，每个菜谱只有一张成品图片，无法点击图片放大图。建议以后拥有自己的社区后，支持用户上传多张成品图可供左右滑动查看。</li>
<li>用户暂时只能点赞收藏菜谱，并不能评论和发布作品，可以让用户购买APP上的食材后，分享该商品的做法，并po出自己的成品图/视频，同时借助评论功能让用户进行交流。</li>
<li>由于大多是第三方APP的用户在社区上发布的作品，所以还没有关注功能。</li>
<li>UGC区域的内容大多源于豆果美食这一第三方APP，相当于是把豆果美食的社区生态圈硬搬到自己的平台。我建议每日优鲜后期可以形成自己的社区，让自己的用户在“吃什么”页面发布作品。前期，为了加大宣传，可以邀请一些明星入驻，让明星在“吃什么”社区分享自己的作品。</li>
</ol>
<h2 id="toc-6">五、总结</h2>
<p>随着互联网发展的越来越成熟，生鲜电商作为生鲜流通新渠道，发展速度快，成长空间广阔，导致新的生鲜电商不断增加，巨头布局持续扩大，行业竞争还在持续升级。每日优鲜从思路、模式到路径，都需要创新，才能在众多生鲜平台中脱颖而出。</p>
<p>注：文档中所引用的APP截图均来源于“每日优鲜”APP，原型图均为作者自己制作。</p>
<p> </p>
<p>本文由 @Luffy 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自网络</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="3513434" data-author="1043503" data-avatar="https://static.woshipm.com/APP_U_202003_20200312215935_3355.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://image.woshipm.com//wp-files/2015/10/touxiang-3.jpg!avatar" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            