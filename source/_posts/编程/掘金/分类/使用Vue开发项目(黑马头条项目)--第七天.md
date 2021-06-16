
---
title: '使用Vue开发项目(黑马头条项目)--第七天'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0203c3ae5f5843aa984e1a6fdc18a239~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 07:16:57 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0203c3ae5f5843aa984e1a6fdc18a239~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>需要实现的主要功能如下：</p>
<blockquote>
<p>资讯列表、标签页切换，文章举报，频道管理、文章详情、阅读记忆，关注功能、点赞功能、评论功能、回复评论、搜索功能、登录功能、个人中心、编辑资料、小智同学 ...</p>
</blockquote>
<blockquote>
<p>今天要实现的功能主要是：文章详情，关注功能，点赞功能，评论功能</p>
</blockquote>
<h2 data-id="heading-0">1 文章详情功能</h2>
<h3 data-id="heading-1">1.1 创建<code>views/article/article.vue</code> 并写入以下内容</h3>
<pre><code class="copyable"><template>
  <div class="article-container">
    <!-- 导航栏 -->
    <van-nav-bar
      fixed
      left-arrow
      @click-left="$router.back()"
      title="文章详情"
    ></van-nav-bar>
    <!-- /导航栏 -->

    <!-- 加载中 loading -->
    <van-loading class="article-loading" />
    <!-- /加载中 loading -->

    <!-- 文章详情 -->
    <div class="detail">
      <h3 class="title">标题</h3>
      <div class="author">
        <van-image round width="1rem" height="1rem" fit="fill" />
        <div class="text">
          <p class="name">作者</p>
          <p class="time">4天前</p>
        </div>
        <van-button
          round
          size="small"
          type="info"
        >+ 关注</van-button>
      </div>
      <div class="content">
        <div>正文</div>
      </div>
      <van-divider>END</van-divider>
      <div class="zan">
        <van-button round size="small" hairline type="primary" plain icon="good-job-o">点赞</van-button>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <van-button round size="small" hairline type="danger" plain icon="delete">不喜欢</van-button>
      </div>
    </div>
    <!-- /文章详情 -->

  </div>
</template>

<script>
export default &#123;
  name: 'ArticleIndex',
  data () &#123;
    return &#123;
      loading: true, // 控制加载中的 loading 状态
      article: &#123; &#125;
    &#125;
  &#125;
&#125;
</script>

<style scoped lang='less'>
.article-container&#123;
  position: absolute;
  left: 0;
  top: 0;
  overflow-y: scroll;
  width: 100%;
  height: 100%;
&#125;
.article-loading &#123;
  padding-top: 100px;
  text-align: center;
&#125;
.error&#123;
  padding-top: 100px;
  text-align: center;
&#125;
.detail &#123;
  padding: 50px 10px;
  .title &#123;
    font-size: 16px;
  &#125;
  .zan&#123;
    text-align: center;
  &#125;
  .author &#123;
    padding: 10px 0;
    display: flex;
    .text &#123;
      flex: 1;
      padding-left: 10px;
      line-height: 1.3;
      .name &#123;
        font-size: 14px;
        margin: 0;
      &#125;
      .time &#123;
        margin: 0;
        font-size: 12px;
        color: #999;
      &#125;
    &#125;
  &#125;
  .content &#123;
    font-size:14px;
    overflow: hidden;
    white-space: pre-wrap;
    word-break: break-all;
    /deep/ img&#123;
      max-width:100%;
      background: #f9f9f9;
    &#125;
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2路由配置</h3>
<pre><code class="copyable">  &#123;
    path: '/article/:id', // 动态路由
    name: 'article',
    component: () => import('../views/article/article.vue')
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.3 测试效果</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0203c3ae5f5843aa984e1a6fdc18a239~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">1.4 文章详情-路由跳转</h3>
<p><strong><code>views/home/articleList.vue</code>中，点击文章列表项的时候，传递文章id跳转到文章详情页</strong></p>
<pre><code class="copyable"><van-cell
   v-for="(item,idx) in list"
   :key="idx"
   :title="item.title"
+  @click="$router.push('/article/' + item.art_id)"
>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.5 文章详情-获取数据并显示</h3>
<h4 data-id="heading-6">1.5.1 封装接口</h4>
<p><strong>在 <code>api/article.js</code> 中新增一个方法</strong></p>
<pre><code class="copyable">/**
 * 获取文章详情
 * @param &#123;*&#125; articleId
 */
export const getDetail = articleId => &#123;
  return request(&#123;
    method: 'GET',
    url: 'v1_0/articles/' + articleId
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">1.5.2 调用接口</h4>
<p><strong>在<code>views/article/article.vue</code>组件中调用接口，获取文章详情</strong></p>
<pre><code class="copyable">created () &#123;
    this.loadDetail()
  &#125;,
  methods: &#123;
    async loadDetail () &#123;
      try &#123;
        this.loading = true
        const res = await getDetail(this.$route.params.id)
        this.article = res.data.data
        this.loading = false
      &#125; catch (err) &#123;
        this.loading = false
        console.log(err)
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">1.5.3 更改模板，渲染页面</h4>
<pre><code class="copyable"><!-- 导航栏 -->
    <van-nav-bar
      fixed
      left-arrow
      @click-left="$router.back()"
      :title="'文章详情-'+ article.title"
    ></van-nav-bar>
    <!-- /导航栏 -->

    <!-- 加载中 loading -->
    <van-loading v-if="loading" class="article-loading" />
    <!-- /加载中 loading -->

    <!-- 文章详情 -->
    <div class="detail">
      <h3 class="title">&#123;&#123;article.title&#125;&#125;</h3>
      <div class="author">
        <van-image round width="1rem" height="1rem" fit="fill" />
        <div class="text">
          <p class="name">&#123;&#123;article.aut_name&#125;&#125;</p>
          <p class="time">&#123;&#123;article.pubdate | relativeTime&#125;&#125;</p>
        </div>
        <van-button
          round
          size="small"
          type="info"
        >+ 关注</van-button>
      </div>
      <div class="content">
        <div v-html="article.content"></div>
      </div>
      <van-divider>END</van-divider>
      <div class="zan">
        <van-button round size="small" hairline type="primary" plain icon="good-job-o">点赞</van-button>
      </div>
    </div>
    <!-- /文章详情 -->
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：</p>
<ul>
<li>文章正文是html格式字符串，需要用<strong>v-html</strong>才能正确显示</li>
<li>相对时间处理：直接使用我们在前面定义的<strong>全局过滤器</strong>即可。</li>
</ul>
</blockquote>
<h4 data-id="heading-9">1.5.4 查看效果</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f287f238c1f4ff9b14e3862cd89529f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">2 文章操作-关注&取关</h2>
<blockquote>
<ul>
<li>如果is_followed为 false 表示当前登陆用户并没有关注过本文章的作者。</li>
<li>如果is_followed为true 表示当前登陆用户已经关注过本文章的作者</li>
</ul>
</blockquote>
<h3 data-id="heading-11">2.1封装接口</h3>
<p><strong>在 <code>api/user.js</code> 中新增两个方法：</strong></p>
<pre><code class="copyable">// 关注
export const follow = userId => &#123;
  return request(&#123;
    url: '/v1_0/user/followings', // 接口地址
    method: 'POST', // 方式
    data: &#123;
      target: userId
    &#125;
  &#125;)
&#125;

// 取关
export const unfollow = userId => &#123;
  return request(&#123;
    url: '/v1_0/user/followings/' + userId, // 接口地址
    method: 'DELETE' // 方式
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2.2调用接口</h3>
<p><strong>在<code>\views\article\article.vue</code>模板中</strong></p>
<pre><code class="copyable"><van-button
          round
          size="small"
          type="info"
+         @click="toggleFollow"
+        >&#123;&#123;article.is_followed ? '取关' : '+ 关注'&#125;&#125;</van-button>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">async toggleFollow () &#123;
      try &#123;
        // 检查当前的状态
        const isFollowed = this.article.is_followed
        const userId = this.article.aut_id
        console.log(isFollowed)
        if (isFollowed) &#123;
          //   取关
          await unfollow(userId)
        &#125; else &#123;
          await follow(userId)
        &#125;
        // 更新视图
        //  1. 整体重发请求？（没有必要）
        //  2. 直接修改本地数据is_followed
        this.article.is_followed = !isFollowed
        this.$toast.success('操作成功')
      &#125; catch (err) &#123;
        console.log(err)
        this.$toast.fail('操作失败')
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">2.3 效果图</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfa21598077943ac907c2371582218a1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">3 文章操作-点赞&取消点赞</h2>
<blockquote>
<p>从后端取回来的文章详情中有一个attitude属性用来描述用户对文章的态度，具体是：<code>&#123;-1:无态度,0:不喜欢,1:点赞&#125;</code>。</p>
<p>如果是做点赞，就是把attitude改成1 。取消点赞，变成无态度，就是把 attiude改成 -1。</p>
<p>对应的，视图上有两个地方要修改：</p>
<ul>
<li>文案</li>
<li>图标</li>
</ul>
</blockquote>
<h3 data-id="heading-15">3.1 封装接口</h3>
<p><strong>在 <code>api/article.js</code> 中封装数据接口</strong></p>
<pre><code class="copyable">/**
 * 取消点赞
 * @param &#123;*&#125; id 文章编号
 */
export const deleteLike = id => &#123;
  return request(&#123;
    method: 'DELETE',
    url: 'v1_0/article/likings/' + id
  &#125;)
&#125;

/**
 * 添加点赞
 * @param &#123;*&#125; id 文章编号
 */
export const addLike = id => &#123;
  return request(&#123;
    method: 'POST',
    url: 'v1_0/article/likings',
    data: &#123;
      target: id
    &#125;
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">3.2 调用接口</h3>
<p><strong>然后在 <code>views/article/article.vue</code> 组件中</strong></p>
<pre><code class="copyable"><template>

    <van-button round size="small"
        hairline
        type="primary"
        plain
        :icon="article.attitude === 1 ? 'good-job': 'good-job-o'"
        @click="toggleLike">&#123;&#123; article.attitude == 1 ? '取消点赞' : '点赞' &#125;&#125;     </van-button>
      
</template>

<script>
import &#123; addLike, deleteLike &#125; from '@/api/article'

export default &#123;
  // ...
  methods: &#123;
     async toggleLike () &#123;
      try &#123;
        // 检查当前的状态
        const attitude = this.article.attitude
        const artId = this.article.art_id
        if (attitude === 1) &#123;
          await deleteLike(artId)
          this.article.attitude = -1
        &#125; else if (attitude === -1) &#123;
          await addLike(artId)
          this.article.attitude = 1
        &#125;
        this.$toast.success('操作成功')
      &#125; catch (err) &#123;
        console.log(err)
        this.$toast.fail('操作失败')
      &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">3.3 效果图</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64a43d255ba547af920b19dcacf4db88~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">4 处理404</h2>
<h3 data-id="heading-19">4.1<strong>在<code>views/article/article.vue</code> 组件中</strong></h3>
<pre><code class="copyable">return &#123;
+     is404: false, // 文章是否存在
      loading: true, // 控制加载中的 loading 状态
      article: &#123; &#125; // 当前文章
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">async loadDetail () &#123;
  try &#123;
    this.is404 = false

    this.loading = true
    const &#123;data:&#123;data&#125;&#125; = await getDetail(this.$route.params.id)
    this.article = data
    this.loading = false
  &#125; catch (err) &#123;
    this.loading = false
    console.dir(err)
    // 如何去判断本次请求是404?
    if (err.response.status === 404) &#123;
      this.is404 = true
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> <!-- 加载中 loading -->
    <van-loading v-if="loading" class="article-loading" />
    <!-- 加载中 loading -->

    <div class="error" v-if="is404">
      <p>文章被外星人吃掉了</p>
      <van-button @click="$router.back()">后退</van-button>
      <van-button @click="$router.push('/')">回主页</van-button>
    </div>
    <!-- 文章详情 -->
    <div class="detail" v-else>
       // 省略 -----
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">效果图</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05cbe388140c4cd9904c2a3ed72236ef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-21">5 文章评论</h2>
<h3 data-id="heading-22">5.1 基本布局</h3>
<p><strong>article/comment.vue  添加一个组件来完成评论列表功能</strong></p>
<pre><code class="copyable"><template>
  <div class="article-comments">
    <!-- 评论列表 -->
    <van-list
      v-model="loading"
      :finished="finished"
      finished-text="没有更多了"
      @load="onLoad"
    >
      <van-cell
        v-for="item in list"
        :key="item.com_id"
        >
        <van-image
          slot="icon"
          round
          width="30"
          height="30"
          style="margin-right: 10px;"
          :src="item.aut_photo"
        />
        <span style="color: #466b9d;" slot="title">&#123;&#123;item.aut_name&#125;&#125;</span>
        <div slot="label">
          <p style="color: #363636;">&#123;&#123;item.content&#125;&#125;</p>
          <p>
            <span style="margin-right: 10px;">&#123;&#123;item.pubdate | relativeTime &#125;&#125;</span>
          </p>
        </div>
        <van-icon slot="right-icon" name="like-o" />
      </van-cell>
    </van-list>
    <!-- 评论列表 -->
    <!-- 发布评论 -->
    <div :class="commentShow ? 'art-cmt-container-1' : 'art-cmt-container-2'">
      <!-- 底部添加评论区域 - 1 -->
      <div class="add-cmt-box van-hairline--top">
        <van-icon name="arrow-left" size="24px" @click="$router.back()" />
        <div class="ipt-cmt-div">发表评论</div>
        <div class="icon-box">
          <van-badge content="10" max="99">
            <van-icon
              name="comment-o"
              size="24px"
            />
          </van-badge>
          <van-icon name="star-o"  size="24px" />
          <van-icon name="share-o" size="24px" />
        </div>
      </div>

      <!-- 底部添加评论区域 - 2 -->
      <div class="cmt-box van-hairline--top" v-show="!commentShow">
        <textarea
          placeholder="友善评论、理性发言、阳光心灵"
          v-model.trim="commentText"
        ></textarea>
        <van-button
          type="default"
          >发布</van-button>
      </div>
    </div>
    <!-- /发布评论 -->
  </div>
</template>

<script>
export default &#123;
  name: 'ArticleComment',
  data () &#123;
    return &#123;
      commentText: '',
      commentShow: true,
      list: [], // 评论列表
      loading: false, // 上拉加载更多的 loading
      finished: false // 是否加载结束
    &#125;
  &#125;,

  methods: &#123;
    onLoad () &#123;
      // 异步更新数据
      // setTimeout 仅做示例，真实场景中一般为 ajax 请求
      setTimeout(() => &#123;
        for (let i = 0; i < 10; i++) &#123;
          this.list.push(this.list.length + 1)
        &#125;

        // 加载状态结束
        this.loading = false

        // 数据全部加载完成
        if (this.list.length >= 40) &#123;
          this.finished = true
        &#125;
      &#125;, 1000)
    &#125;
  &#125;
&#125;
</script>

<style scoped lang='less'>
// 发表评论的区域是固定在下端的
.publish-wrap &#123;
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
&#125;
// 给发表评论区空出地方
.van-list &#123;
  margin-bottom: 45px;
&#125;

/*美化 - 文章详情 - 底部的发布评论-样式 */
// 外层容器
.art-cmt-container-1 &#123;
  padding-bottom: 46px;
&#125;
.art-cmt-container-2 &#123;
  padding-bottom: 80px;
&#125;

// 发布评论的盒子 - 1
.add-cmt-box &#123;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  box-sizing: border-box;
  background-color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 46px;
  line-height: 46px;
  padding-left: 10px;
  .ipt-cmt-div &#123;
    flex: 1;
    border: 1px solid #efefef;
    border-radius: 15px;
    height: 30px;
    font-size: 12px;
    line-height: 30px;
    padding-left: 15px;
    margin-left: 10px;
    background-color: #f8f8f8;
  &#125;
  .icon-box &#123;
    width: 40%;
    display: flex;
    justify-content: space-evenly;
    line-height: 0;
  &#125;
&#125;

.child &#123;
  width: 20px;
  height: 20px;
  background: #f2f3f5;
&#125;

// 发布评论的盒子 - 2
.cmt-box &#123;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  padding-left: 10px;
  box-sizing: border-box;
  background-color: white;
  textarea &#123;
    flex: 1;
    height: 66%;
    border: 1px solid #efefef;
    background-color: #f8f8f8;
    resize: none;
    border-radius: 6px;
    padding: 5px;
  &#125;
  .van-button &#123;
    height: 100%;
    border: none;
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">5.2 注册并引入</h3>
<p><strong>在文章详情页面src\views\article\article.vue中加载注册文章评论子组件：</strong></p>
<pre><code class="copyable">import ArticleComment from './comment'

export default &#123;
  ...
  components: &#123;
    ArticleComment
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><div class="article-container">
...  
    <!-- 文章评论 -->
    <article-comment></article-comment>
    <!-- 文章评论 -->
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果图</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/369691dc08bd43ca978ae85f6fb98280~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24">5.3获取文章评论数据并显示</h3>
<p><strong>在 <code>api/comment.js</code> 中封装请求方法</strong></p>
<pre><code class="copyable">/**
 * 获取评论
 * @param &#123;*&#125; articleId
 * @param &#123;*&#125; offset
 */
export const getComment = (articleId, offset) => &#123;
  return request(&#123;
    method: 'GET',
    url: '/v1_0/comments',
    params: &#123;
      type: 'a',
      source: articleId,
      offset
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">5.4 加载获取数据</h3>
<p><strong>在 <code>views/article/comment.vue</code> 组件中加载获取数据</strong></p>
<pre><code class="copyable">// 数据项
data () &#123;
  return &#123;
+   total_count: 10,
+   offset: null, // 获取评论数据的偏移量，值为评论id，表示从此id的数据向后取，不传表示从第一页开始读取数据
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import &#123; getComments &#125; from '@/api/comment'
async onLoad () &#123;
  try &#123;
      // 1. 发请求
      const &#123;data:&#123;data&#125;&#125; = await getComments(this.$route.params.id, this.offset)
      const arr = data.results
      // 2. 追加到list
      this.list.push(...arr)
      // 3. loading <-false
      this.loading = false
      // 4. 判断是否加载完成
      this.finished = !arr.length
      // 5. 更新offset
      this.offset = data.last_id
      // 6. 总数
      this.total_count = data.total_count
  &#125; catch (error) &#123;
    this.$toast('获取评论失败')
    this.loading = false
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>模板绑定</strong></p>
<pre><code class="copyable"><van-cell
        v-for="item in list"
        :key="item.com_id"
        >
        <van-image
          slot="icon"
          round
          width="30"
          height="30"
          style="margin-right: 10px;"
          :src="item.aut_photo"
        />
        <span style="color: #466b9d;" slot="title">&#123;&#123;item.aut_name&#125;&#125;</span>
        <div slot="label">
          <p style="color: #363636;">&#123;&#123;item.content&#125;&#125;</p>
          <p>
            <span style="margin-right: 10px;">&#123;&#123;item.pubdate | relativeTime &#125;&#125;</span>
            <van-button size="mini" type="default">回复</van-button>
          </p>
        </div>
        <van-icon slot="right-icon" name="like-o" />
      </van-cell>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果图</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba45d711d49b4cae831c616457d13d16~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-26">6 发布文章评论-基本交互</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/032cf95eaf5c4f2c996100eb5db2a84b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>用boolean来控制两个状态的切换</p>
<p>（1）点击发表评论：从状态1---> 状态2</p>
<p>（2）输入框失去焦点时，状态2 ----> 状态1</p>
</blockquote>
<h3 data-id="heading-27">6.1 视图</h3>
<pre><code class="copyable"><!-- 底部添加评论区域 - 1 -->
<div class="add-cmt-box van-hairline--top" v-show="commentShow">
<!-- 底部添加评论区域 - 2 -->     
<div class="cmt-box van-hairline--top" v-show="!commentShow">
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">6.2 添加事件及属性</h3>
<pre><code class="copyable"><!-- 发布评论 -->
    <div :class="commentShow ? 'art-cmt-container-1' : 'art-cmt-container-2'">
      <!-- 底部添加评论区域 - 1 -->
  +   <div class="add-cmt-box van-hairline--top" v-show="commentShow">
        <van-icon name="arrow-left" size="24px" @click="$router.back()" />
  +     <div class="ipt-cmt-div" @click="hShowCommentArea">发表评论</div>
        <div class="icon-box">
          <van-badge content="10" max="99">
            <van-icon name="comment-o" size="24px" />
          </van-badge>
          <van-icon name="star-o" size="24px" />
          <van-icon name="share-o" size="24px" />
        </div>
      </div>

      <!-- 底部添加评论区域 - 2 -->
      <div class="cmt-box van-hairline--top" v-show="!commentShow">
        <textarea
 +        ref="txt"
 +        @blur="hBlur"
          placeholder="友善评论、理性发言、阳光心灵"
          v-model.trim="commentText"
        ></textarea>
 +      <van-button type="default" @click="hAddComment">发布</van-button>
      </div>
    </div>
    <!-- /发布评论 -->
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">6.3 执行代码</h3>
<pre><code class="copyable">// 用户点击添加
    hAddComment () &#123;
      alert('hAddComment')
    &#125;,
    // 输入框失去焦点
    hBlur () &#123;
      // 回到状态1
      // this.$nextTick(() => &#123;
      //   this.commentShow = true
      // &#125;)
      setTimeout(() => &#123;
        this.commentShow = true
      &#125;)
    &#125;,
    // 用户点击了发表评论
    hShowCommentArea () &#123;
      // 状态2会显示出来
      this.commentShow = false // 通知视图 等会 去更新
      // $nextTick(回调函数)  // 更新视图之后，去执行回调函数
      this.$nextTick(() => &#123;
        // 让输入框获取焦点
        this.$refs.txt.focus()
      &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">6.4 发布文章评论</h3>
<p><strong>在 <code>api/comment.js</code> 中添加封装数据接口</strong></p>
<pre><code class="copyable">import request from '@/utils/request.js'

/**
 * 添加文章评论
 * @param &#123;*&#125; articleId
 * @param &#123;*&#125; content
 */
export const addComment = (articleId, content) => &#123;
  return request(&#123;
    method: 'POST',
    url: 'v1_0/comments',
    data: &#123;
      target: articleId,
      content
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在 <code>comment.vue</code> 组件中，hAddComment</strong></p>
<pre><code class="copyable">// 用户点击添加
    async hAddComment () &#123;
      if (!this.commentText) &#123;
        return
      &#125;

      try &#123;
        const &#123;data:&#123;data&#125;&#125; = await addComment(this.$route.params.id, this.commentText)
        this.$toast.success('添加评论成功')

        // data.new_obj // 当前评论数据
        this.list.unshift(data.new_obj)

        // 更新页面
      &#125; catch (err) &#123;
        console.log(err)
        this.$toast.fail('添加评论失败')
      &#125;
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">6.5 实现发布评论===>滚动条滚动到发布评论位置</h3>
<p><strong>在comment.vue最上层加入一个id="scrollTh"的div</strong></p>
<pre><code class="copyable"><div id="scrollTh"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> // 用户点击添加
    async hAddComment () &#123;
      if (!this.commentText) &#123;
        return
      &#125;
      try &#123;
        const res = await addComment(this.$route.params.id, this.commentText)
        console.log(res)
        this.$toast.success('添加评论成功')
        this.list.unshift(res.data.data.new_obj)
        // 滚动条滚动到评论发布的位置
+       this.$el.querySelector('#scrollTh').scrollIntoView(&#123;
          // top: 0,
          // el: '#scrollTh',
+         behavior: 'smooth', // 平滑过渡
+         block: 'start' // 上边框与视窗顶部平齐。默认值
+       &#125;)
        // 更新页面
      &#125; catch (err) &#123;
        console.log(err)
        this.$toast.fail('添加评论失败')
      &#125;
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">7 文章评论-点赞</h2>
<blockquote>
<p>在后端接口取出回来的数据中，有一个特殊的字段<code>is_liking</code>表示当前用户对当前评论是否喜欢。</p>
<ol>
<li>从接口中取出数据之后，根据is_liking这个字段来来更新视图</li>
<li>用户点击之后，调用接口去修改is_liking这个字段在服务器上的值，并更新视图。</li>
</ol>
</blockquote>
<h3 data-id="heading-33">7.1 封装接口</h3>
<p><strong>在 <code>api/comment.js</code> 中添加两个方法</strong></p>
<pre><code class="copyable">/**
 * 对文章评论进行点赞
 * @param &#123;*&#125; commentId 评论id
 */
export const addCommentLike = commentId => &#123;
  return request(&#123;
    method: 'POST',
    url: 'v1_0/comment/likings',
    data: &#123;
      target: commentId
    &#125;
  &#125;)
&#125;

/**
 * 取消文章评论的点赞
 * @param &#123;*&#125; commentId 评论id
 */
export const deleteCommentLike = commentId => &#123;
  return request(&#123;
    method: 'DELETE',
    url: 'v1_0/comment/likings/' + commentId
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">7.2 修改视图</h3>
<p><strong>在 <code>views/article/comment.vue</code> 组件中：</strong></p>
<pre><code class="copyable"><van-icon
       slot="right-icon"
       :name="item.is_liking ? 'like' : 'like-o'"
       @click="hToggleLike(item)"
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">7.3 具体实现代码</h3>
<pre><code class="copyable"><script>
import &#123;
  getComments,
  addComment,
+  addCommentLike,
+  deleteCommentLike
&#125; from '@/api/comment'

export default &#123;
  methods: &#123;
    // 用户喜欢/取消喜欢评论
    async hToggleLike (item) &#123;
      try &#123;
        const isLiking = item.is_liking
        const commentId = item.com_id
        if (isLiking) &#123;
          await deleteCommentLike(commentId)
        &#125; else &#123;
          await addCommentLike(commentId)
        &#125;
        this.$toast.success('操作成功')

        // 更新本地数据
        item.is_liking = !isLiking
      &#125; catch (err) &#123;
        console.log(err)
        this.$toast.fail('操作失败')
      &#125;
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果图</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/106380833c594dc7b23d47f97c37552f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            