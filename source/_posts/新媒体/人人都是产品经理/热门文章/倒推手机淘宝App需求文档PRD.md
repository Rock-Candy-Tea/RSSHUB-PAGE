
---
title: '倒推手机淘宝App需求文档PRD'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/TQv8WZYGZ6XO9HPnp3Za.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 26 May 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/TQv8WZYGZ6XO9HPnp3Za.jpg'
---

<div>   
<blockquote><p>本文根据淘宝app的底导航中五个主要模块以及从浏览商品到订单提交做了一个需求分析文档。包括：文档综述、需求整理、需求结构、全局说明、主要功能说明。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-3914924" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/TQv8WZYGZ6XO9HPnp3Za.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>手机淘宝作为目前最大的电商平台，打败了线下实体商店，给了广大群众最方便快捷的购物体验。</p>
<p>人们不用出门就可以买到想要的并且比实体店实惠很多的东西，用户想买的东西在淘宝都能找到，比如衣服、母婴用品、电子产品、化妆品等；想不到的东西在淘宝也能找到，比如教育视频、代写、专家指导、农村特产等。</p>
<p>不论吃的喝的穿的用的玩的学的都可以在这个大平台里满足你。</p>
<p>由于目前淘宝功能模块太多，此次我通过体验和分析这款app，根据淘宝app的底导航中五个主要模块以及从浏览商品到订单提交做一个简单的需求分析文档。</p>
<p><strong>目录</strong></p>
<ul>
<li>一、文档综述</li>
<li>1.版本修订记录</li>
<li>2.文档输入环境</li>
<li>3.产品介绍</li>
<li>4.产品用户分析</li>
<li>二、需求整理</li>
<li>1.用户需求分析</li>
<li>2.目标用户</li>
<li>3.需求汇总</li>
<li>三、需求结构</li>
<li>1.产品功能架构图</li>
<li>2.产品信息架构图</li>
<li>3.产品登录注册流程图</li>
<li>4.商品购买流程图</li>
<li>四、全局说明</li>
<li>1.功能权限</li>
<li>2.键盘权限</li>
<li>3.页面内交互</li>
<li>4.内容提示</li>
<li>五、主要功能说明</li>
<li>1.登录注册</li>
<li>2.首页</li>
<li>3.商品详情页</li>
<li>4.购物车页面</li>
<li>5.订单页面</li>
<li>六、总结</li>
</ul>
<h2 id="toc-1">一、产品综述</h2>
<h3>1. 版本修订记录</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/iFZXlpUTCkbyPCTZb4RE.png" alt width="316" height="103" referrerpolicy="no-referrer"></p>
<h3>2. 文档输入环境</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/0ZCXRnXe4RhXQ4Ju0xOV.jpeg" alt width="606" height="225" referrerpolicy="no-referrer"></p>
<h3>3. 产品介绍</h3>
<p>手机淘宝是一个综合网购平台，聚集了商品浏览、购物车、购买、收藏、管理、地址管理、订单查询、退换货、直播、聚划算等功能。淘宝包含了各大类型的品牌以及个人商家入驻，满足不同年级阶段用户的不同需求，并会针对用户的喜好特点推荐相似商品，给用户最特色化的体验。</p>
<h3>4. 产品用户分析</h3>
<p>在如今的互联网时代，网上购物已经非常普遍，淘宝旨在为用户打造一个全方位的购物平台满足不同年龄阶段不用资产阶级用户的需求。</p>
<p>App store查看的产品特色：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/cQN4GIEfruoldVi6nAg5.jpg" alt width="602" height="953" referrerpolicy="no-referrer"></p>
<p>下载量排行：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/wABClpqDo7CEmWpn8FsO.png" alt width="801" height="210" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">数据来源：艾瑞数据</p>
<p>淘宝近半年搜索指数：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/BNPPnKoxi4ilwxLcpWiB.png" alt width="800" height="366" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">数据来源：百度指数</p>
<p>由上图可以看出：用户在周一至周四的购买量以及淘宝浏览量相比周五至周日要低很多。</p>
<p>一方面一般的快的时间为三天，用户为了在节假日内拿到想要的商品会选择周五购买，图中“E”值即为周五的搜索指数。另一方面用户在周末的时候内有大量的时间浏览淘宝以及购买商品，所以周末的搜索指数高于工作日，这样也会大大减少用户去实体店的欲望。</p>
<p>同行指数近半年对比：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/rRNi9dy1WDoFG8FoNn4U.png" alt width="801" height="479" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">数据来源：百度指数</p>
<p>根据当前最热门的电商移动平台作为对比，由上图可以看出，在淘宝、京东、拼多多、苏宁易购、唯品会五大电商品台的对比下，淘宝的指数明显低于京东，高于其他平台。</p>
<p>这也说明现在的电商品台层出不穷，京东和拼多多对淘宝的冲击力还是很大的。京东旨在让用户更加快速的买到正品，它的物流速度和品质保证是最大的亮点。</p>
<p>而拼多多则相反，拼多多服务的是低收入人群，大家为了一个商品可以选择和朋友拼单以最低价购买，这一特点让拼多多迅速跻身于三大电商平台之一。</p>
<p>为了跟随时代不断进步，淘宝随时都需要关注着用户的喜好和潜在的需求。</p>
<p>近一年人群画像：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/QCon7rsjpIROKmFZEMCO.png" alt width="800" height="328" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">数据来源：百度指数</p>
<p>由上图可以看出：北上广深等一线大城市使用淘宝的频率非常高，而二三线城市也非常喜欢使用淘宝。所以淘宝的覆盖地区非常广。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/qMmcwrmGVZk6zsYG4zZJ.png" alt width="804" height="377" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/oQqjaGbL652KAI8OU6pe.png" alt width="807" height="424" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">数据来源：移动观象台</p>
<p>由上图可以看出：最爱使用淘宝的年龄阶段以20-35岁之间的年轻人为主，而且女性居多，但是男女比例差并不明显，所以在淘宝购物的男性群体也是很多的。</p>
<p><strong>总结：</strong></p>
<ul>
<li>手机淘宝是目前下载量最高的电商移动平台，排名第四，前三依次为微信、QQ、支付宝。</li>
<li>在淘宝等移动电商APP的冲击下，实体店处于劣势，用户更加中意在网上购买喜欢的商品。</li>
<li>在京东和拼多多两面夹击下，淘宝依然处于紧张状态。</li>
<li>在经济发达城市，淘宝的使用率很高，淘宝覆盖了高中低消费群体。</li>
<li>20-35岁的年轻人为主要的消费群体，女性比例微微高于男性。</li>
</ul>
<h2 id="toc-2">二、需求整理</h2>
<h3>1. 用户需求分析</h3>
<p>随着互联网行业的兴起，人们的生活变得越来越方便了，最新新闻浏览、嘀嘀打车、外卖订餐、远程办公以及电商等等。</p>
<p>我们足不出户就可以了解到世界各地的新闻，购买到世界各地的产品。越来越多的人喜欢在网上购买商品，方便快捷，质量有保证还可以七天退换。</p>
<p>淘宝提供了这样一个平台，让我们可以随心所欲的购买产品，同时淘宝也帮助了成千上万的人自主创业。不管是副业还是主业都给了很多人挣钱的机会，由于淘宝的功能异常多和复杂，我将列出部分</p>
<ul>
<li>商品齐全，随时浏览购买。</li>
<li>实体店商品价格昂贵，退换困难。</li>
<li>观看直播，专业人士讲解，快速了解产品详情。</li>
<li>折扣产品、活动商品、免税商品、国际商品购买。</li>
<li>同城买菜海鲜淘，饿了么订购外卖。</li>
<li>自己当卖家。</li>
<li>其他。</li>
</ul>
<h3>2. 目标用户</h3>
<ul>
<li>没有时间去实体店的用户。</li>
<li>想看到更多好物种草。</li>
<li>想一次性买全各个类别的产品。</li>
<li>有潜在需求有时间玩手机的用户。</li>
<li>想省点钱，中意买价格喜人物美价廉的商品。</li>
<li>大牌折扣能及时了解到。</li>
<li>喜欢做饭的下班晚的上班族以及需要带孩子的家庭主妇。</li>
</ul>
<h3>3. 需求汇总</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/4Foq0sUT5DxpppvAFaVK.png" alt width="801" height="689" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、需求结构</h2>
<h3>1. 产品功能架构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/JeBCnh2OZ2CUgNEWZFzZ.png" alt width="803" height="1507" referrerpolicy="no-referrer"></p>
<h3>2. 产品信息架构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/9Z9TkkNP8X6oEYQK9nGO.png" alt width="801" height="1454" referrerpolicy="no-referrer"></p>
<h3>3. 产品登录注册流程图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/YVaBL5rocvFoXPF64cN1.png" alt width="604" height="671" referrerpolicy="no-referrer"></p>
<h3>4. 商品购买流程图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/06wovQHmD4xFTp788mxt.png" alt width="602" height="736" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、全局说明</h2>
<h3>1. 功能权限</h3>
<p><strong>4.1.1 未登录状态下</strong></p>
<ul>
<li>不能加入购物车、购买商品；无法客服聊天、收藏、查看微淘上新、我的关注。</li>
<li>不能进入“我的”、“消息”、“购物车”、“会员码”页面，点击直接进入登录页面。<br>
进行以上操作都会转跳到登录页。</li>
</ul>
<p><strong>4.1.2 登录状态下</strong></p>
<p>可进行任何操作</p>
<h3>2. 键盘权限</h3>
<ul>
<li>点击手机注册或者手机登录时，输入框时弹出数字键盘；</li>
<li>点击账号密码登录、搜索框、评论框、聊天框时⻚面底部弹出字母全键盘。</li>
</ul>
<h3>3. 页面内交互</h3>
<p><strong>4.3.1 底导航切换</strong></p>
<p>位置：底导航固定在手机页面最底部。</p>
<p>交互：</p>
<ul>
<li>用户在点击“我的”、“微淘”、“消息”、“购物车”、“我的淘宝”进入到对应的模块中。</li>
<li>选中的按钮文字变为红色。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/S08sQvIHtAC6AHRx9ukQ.gif" alt width="396" height="682" referrerpolicy="no-referrer"></p>
<p><strong>4.3.2 键盘弹出</strong></p>
<p>位置：弹窗固定在手机页面底部。</p>
<p>交互：</p>
<ul>
<li>点击【搜索框】，页面底部交互页面变暗，弹窗由底部向上弹出。</li>
<li>点击【取消】回到上级页面。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/wFrEc8ZWVh5YNzvHe84g.gif" alt width="394" height="678" referrerpolicy="no-referrer"></p>
<p><strong>4.3.3 商品搜索</strong></p>
<p>位置：搜索框位于页面导航栏中间。</p>
<p>交互：</p>
<ul>
<li>当用户点击【搜索框】时，弹出键盘，点击【完成】后进入“搜索”页面。</li>
<li>点击【返回】返回上级页面。</li>
<li>点击【取消】搜索页面由上至下消失，父级页面淘宝主页显示出来。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/SpieGwtV5gTSkKfd5K0L.gif" alt width="396" height="673" referrerpolicy="no-referrer"></p>
<p><strong>4.3.4 导航栏显示和定位</strong></p>
<p>位置：导航栏随着用户对页面的滑动显示和隐藏在页面的固定位置。</p>
<p>交互：</p>
<ul>
<li>当用户向上滑动屏幕时，导航栏逐渐显示。</li>
<li>页面滑动或用户滑动页面至顶部时，导航栏逐渐隐藏。</li>
<li>用户点击导航栏按钮时，页面滑动至对应区域，下划线滑动至导航栏对应按钮。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/gtmXJtENTffCpPXJHQ05.gif" alt width="398" height="678" referrerpolicy="no-referrer"></p>
<p><strong>4.3.5 详情页分享</strong></p>
<p>位置：分享位于导航栏右上角，点击分享弹窗位于手机底部。</p>
<p>交互：</p>
<ul>
<li>点击分享底部弹出分享列表框，用户可以分享至多个平台或者淘宝好友。</li>
<li>图片分享逐渐弹出，用户可以下载分享至其他的平台或好友。</li>
<li>点击暗部区域或者【取消按钮】，分享弹出框逐渐隐藏。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/tZnztqSx7eQn0Pg25iOW.gif" alt width="398" height="680" referrerpolicy="no-referrer"></p>
<p><strong>4.3.6 选择规格加入购物车成功</strong></p>
<p>位置：规格弹出有底部向上弹出，固定于手机底部。</p>
<p>交互：</p>
<ul>
<li>当不需要选择规格时，直接提示添加成功。</li>
<li>当用户点击【加入购物车】后出现规格选择，页面底部交互页面变暗，弹窗由底部向上弹出。</li>
<li>选择规格完成，点击【确定】按钮确认添加至购物车。</li>
<li>用户点击【确定】后，规格弹出隐藏，提示用户添加成功。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/L77tUzMdJGXChhggTuKr.gif" alt width="394" height="678" referrerpolicy="no-referrer"></p>
<p><strong>4.3.7 下订单</strong></p>
<p>位置：下订单按钮，固定于手机底部</p>
<p>交互：</p>
<ul>
<li>点击购物车底导航进入购物车页面进行商品购买操作。</li>
<li>当用户点击单选框或者全选框点击的单选框变为选中状态，如果该店铺被加入购物车的商品只有一个，那么该店铺也变为选中状态，意思就是提示用户该店铺的商品已经被全部选中。</li>
<li>用户可以查看到结算的数量和价格。</li>
<li>选择完成后，点击【结算】按钮进入至确认订单页面。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/kWV4BTkA98V3y38PAVYp.gif" alt width="394" height="672" referrerpolicy="no-referrer"></p>
<h3>4. 内容提示</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/4qLJa8c1j9PRiQfydqAP.png" alt width="600" height="470" referrerpolicy="no-referrer"><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/n1JFMYbYEjeRwVAEkcQY.png" alt width="604" height="478" referrerpolicy="no-referrer"></p>
<p>常用Icon：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/yGx3xJvCxP6H56uA68kd.png" alt width="797" height="249" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、主要功能说明</h2>
<h3>1. 登录注册</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/HGtX4hSEuwEpygVb7zKS.jpg" alt width="799" height="369" referrerpolicy="no-referrer"></p>
<p><strong>5.1.1 页面名称</strong></p>
<p>登录页面、注册页面</p>
<p><strong>5.1.2 页面入口</strong></p>
<p>当用户未登录时，点击“消息”、“购物车”，“我的淘宝”进入登录页面，在主页中，点击【立即登录】、【我的会员码图标】、快捷按钮进入登录页面。在微淘模块中，点击【上新】、【关注】、【我的关注】、【登录】进入登录页面。用户点击立即注册进入注册页面。</p>
<p>当用户登录成功后，不再出现注册登录页面，用户可以在设置中退出登录重新进入登录页面。</p>
<p><strong>5.1.3 页面功能</strong></p>
<p>手机号码、邮箱、用户名登录，支付宝快捷登录、找回会员名、手机号码注册。</p>
<p><strong>5.1.4 页面逻辑</strong></p>
<ul>
<li>登录页面可以提供用户手机号码、邮箱、账户名以及快捷方式登录。</li>
<li>当用户填写好手机号码、邮箱或账户名时，登录按钮变亮即变为可点击状态。</li>
<li>用户可以点击更多选项找回会员名或寻求帮助。</li>
<li>用户不登录时可以正常查看淘宝主页，微淘主页、商品信息、图片、分享、扫一扫。</li>
<li>当用户想进行购买、加入购物车、查看我的、消息、上新和关注、评论、查看会员码时需跳转至登录页面登录。</li>
<li>用户注册时，点击手机号码区域选择可进行区号更换。</li>
<li>当用户开始填写好手机号码时，注册按钮变亮即变为可点击状态。</li>
<li>当用户输入的数字超过11位时，或不符合后台规则时，按钮至灰。</li>
<li>用户输入正确，跳转至验证码输入页面并开始倒计时，超过一分钟则重新验证。</li>
<li>输入验证码页面中，用户点击返回可返回上级页面。</li>
</ul>
<h3>2. 首页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/3a7rDPPVQ0shIuyS5Dw0.jpg" alt width="800" height="667" referrerpolicy="no-referrer"></p>
<p><strong>5.2.1 页面名称</strong></p>
<p>淘宝首页</p>
<p><strong>5.2.2 页面入口</strong></p>
<p>用户打开手机淘宝App时，出现的页面，用户也可点击底导航进入首页。</p>
<p><strong>5.2.3 页面功能</strong></p>
<p>扫一扫、搜索、快捷按钮、商品展示。</p>
<p><strong>5.2.4 页面逻辑</strong></p>
<ul>
<li>首页提供搜素、扫一扫、会员码、快捷按钮入口、商品展示。</li>
<li>搜索框的默认关键字根据用户的购买记录浏览记录更换。</li>
<li>用户上滑下滑均可进行刷新。</li>
<li>当用户上滑时，底导航首页按钮更换，点击可以直接进入最顶部。</li>
<li>当用户上滑至商品展示列表区域时，展示分类栏至于顶部。</li>
<li>扫一扫可以切换AR扫码或拍立淘。</li>
<li>搜索页面同输入框一同显示，当用户返回至搜索页面或进入搜索页面时，输入键盘一同弹出。</li>
<li>商品分类模块中，用户左滑可以看到更多商品分类。</li>
</ul>
<h3>3. 商品详情页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/gYVPkmjGzSMHsHRcqNUD.jpg" alt width="801" height="744" referrerpolicy="no-referrer"></p>
<p><strong>5.3.1 页面名称</strong></p>
<p>商品详情页面</p>
<p><strong>5.3.2 页面入口</strong></p>
<p>用户在首页、微淘、订单等模块点击商品item，或者搜索结果列表进入。</p>
<p><strong>5.3.3 页面功能</strong></p>
<p>搜索、分享、购物车、收藏、联系客服、加入购物车、立即购买。</p>
<p><strong>5.3.4 页面逻辑</strong></p>
<ul>
<li>详情页面是一件商品的详细展示，包含了价格、标题、发货地、商品规格、评价、问答以及详情和推荐方便用户查阅。</li>
<li>用户可以返回上级页面、分享给淘宝朋友或者分享到其他平台。</li>
<li>当用户点击店铺时，进入卖家店铺。</li>
<li>当用户点击客服时进入客服聊天窗口。</li>
<li>点击更多由上至下弹出选择框，用户可以点击按钮进入其他页面比如“消息”、“首页”。</li>
<li>点击加入购物车弹出规格选择框用户选择后提示加入成功，点击立即购买弹出规格选择框用户选择后进入订单提交页面。</li>
<li>用户点击图片进入图片全屏页面，长按可保存图片或查看原图，单击图片可退出全屏，点击【取消】返回详情页面。</li>
<li>点击分享图标时，分享列表有底部弹出，可以分享至微信、朋友圈、QQ、钉钉、支付宝和短信。可以操作复制链接等其他操作。</li>
<li>当用户点击图片右上角的下载按钮，或长按图片可以保存图片至本地相册。</li>
</ul>
<h3>4. 购物车页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/VjDPlYZBam3wRm5ascEf.jpg" alt width="803" height="379" referrerpolicy="no-referrer"></p>
<p><strong>5.4.1 页面名称</strong></p>
<p>购物车页面</p>
<p><strong>5.4.2 页面入口</strong></p>
<p>用户在底导航点击购物车模块、商品详情中点击购物车图标进入购物车页面。</p>
<p><strong>5.4.3 页面功能</strong></p>
<p>管理删除和清理、选择结算、商品查看、数量加减。</p>
<p><strong>5.4.4 页面逻辑</strong></p>
<ul>
<li>购车页面展示了喜欢商品的列表。</li>
<li>用户可以点击管理、管理购物车的数量对商品进行移除和移入收藏夹，用户也可以对某个商品右滑进行一样的操作。</li>
<li>当用户对商品右滑时，出现按钮选择框，点击“删除”，删除当前商品。点击“移入收藏夹”可把商品转移至收藏夹产品中，点击“找相似”可以进入找相似页面。</li>
<li>用户点击店铺名称可以进入店铺主页、点击商品可以进入商品详情页面，点击规格可以重新选择规格。</li>
<li>商品的数量可以通过点击加减按钮实现数量的改变</li>
<li>用户可以选择某个商品点击单选框或者直接点击全选，去结算商品。</li>
</ul>
<h3>5. 订单页面</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/05/2dPhWBmFeEOKB6T71I52.jpg" alt width="802" height="800" referrerpolicy="no-referrer"></p>
<p><strong>5.5.1 页面名称</strong></p>
<p>我的订单页面</p>
<p><strong>5.5.2 页面入口</strong></p>
<p>用户在“我的淘宝”里面可以直接点击某个状态的订单进入订单列表，或者点击【查看全部订单】进入订单列表。</p>
<p><strong>5.5.3 页面功能</strong></p>
<p>搜索订单、删除订单、查看物流、确认收货、追加评价、卖了换钱、申请开票、提醒发货、加入购物车、其他。</p>
<p><strong>5.5.4 页面逻辑</strong></p>
<ul>
<li>用户点击查看商品订单时，【全部】按钮选中，用户可下滑查看全部订单。</li>
<li>用户可以点击其他状态按钮具体查看某个状态的所有订单。</li>
<li>当点击搜索框时，弹出搜索页面用户可以搜索具体订单，点击【取消】搜索框隐藏。</li>
<li>订单商品可以点击进入状态详情页面，或是直接在订单列表点击快捷按钮进行操作。</li>
<li>用户已经购买完成的商品，可以直接点击加入购物车再次购买。</li>
</ul>
<h2 id="toc-6">六、总结</h2>
<p>手机淘宝功能繁多框架庞大，内嵌的平台也很多。包括近些年火起来的直播也是淘宝的一大流量来源之一。</p>
<p>作为淘宝的粉丝，我写的还只是冰山一角，而且经验尚且不足请多包涵。在疫情期间，盒马生鲜、天猫超市、口罩抢购给予了我很大的帮助，以下是我对淘宝的一些看法。</p>
<h3>1. 优点</h3>
<ul>
<li>功能zhon各类齐全。用户可以在app里购物、买菜、看电影、看直播、学习穿搭等，还可以与国际接轨，随时买到世界各地的产品。</li>
<li>购买方便安全。淘宝与支付宝结合增加了安全性，用户通过第三方平台付款。淘宝拥有自己的物流菜鸟裹裹，包裹送货上门，退换货也是上门取货，商品大部分都是可以七天无理由退换，用户可以随心所欲的购买，新推出的88会员还大大降低了购买成品。</li>
<li>分享方便。分享的方式多样化，保证用户可以分享到各个平台。</li>
<li>页面浏览切换流畅。</li>
<li>扫一扫和图片搜素商品精确度高。</li>
<li>可以帮组家人或者家人帮助购买商品。</li>
<li>消息群，随时了解到最新福利。</li>
</ul>
<h3>2. 我的意见</h3>
<ul>
<li>很多模块的导航栏无法所有滑动，比如我的订单里面【全部】到【待付款】只能通过点击。</li>
<li>可以增加一个订单同商品购买分享功能，当用户B想要用户A的某个商品时，用户A可以把自己的订单分享给用户B，当用户B点击后直接进入到用户B的购物车页面，商品被加入到了用户B的购物车页面，规格与用户A购买的一致。</li>
<li>问答区域可以添加是否允许卖家回答的条件。</li>
<li>购物车中的商品超过某个时期还未失效的商品，可以提示用户清理，当用户看到提示并点击的时候，可以进入到该时期的购物车列表中，此时购物车的商品全都是该时期的，用户点击单选按钮或者全选即可删除。当用户点击右上角的【清除筛选条件】即可恢复到正常的购物车列表。</li>
<li>关注的店铺或商品分类，用户可以自己建立分类名称，比如【衣服】、【电子产品】，当用户想去看自己喜欢的店铺或商品时，可以精确查看某个类别的店铺或商品。这样也可给给用户一种独特的感觉。</li>
</ul>
<p> </p>
<p>本文由 @小敏 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="3873037" data-author="1076885" data-avatar="http://image.woshipm.com/wp-files/2021/04/16aJ1ueUmbyRSDubmmRC.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182804_6785.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            