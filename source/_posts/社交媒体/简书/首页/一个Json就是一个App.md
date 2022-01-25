
---
title: '一个Json就是一个App'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://picsum.photos/400/300?random=4024'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=4024'
---

<div>   
<pre><code>**** 原创不易，转载注明出处 ****
</code></pre>
<p>android原生App最大的痛点就是更新周期长，稍有改动，就需要发布新版本，加上审核，最快也要3天后才能让用户看到新模块。</p>
<p>如果能通过后台下发数据创建View，执行操作，就可以很灵活的动态控制页面。</p>
<p>如果下发json，View的数据很好处理，因为android提供的控件类型是有限的，只要枚举出来就可以。但是一个App的操作太多太多，但是不是无限多呢？也不是。</p>
<h3>一、 只有View</h3>
<p>假设开发一个App只需要展示基础控件。</p>
<pre><code class="json">    &#123;
        "name": "TV",
        "content": "文本",
        "color": "#333333",
        "size": "16"
    &#125;
</code></pre>
<p>明显这是一个TextView，指定了显示的文字、颜色和大小。</p>
<pre><code class="json">    &#123;
        "name": "IV",
        "width": "100",
        "height": "100",
        "url": "https://bugly.qq.com/v2/image?id=2c06cba9-7d27-4f1c-8b0d-b932c33deaf3"
    &#125;
</code></pre>
<p>这个就可以生成一个ImageView。如果更细化，还可以指定margin和padding，脑补css。</p>
<p>同理，如果是容器布局，可以扩展一下，加一个子类集合：</p>
<pre><code class="json">    &#123;
        "name": "VLL",
        "children": [
            &#123;
                "name": "TV"
            &#125;,
            &#123;
                "name": "TV"
            &#125;,
            &#123;
                "name": "TV"
            &#125;
        ]
    &#125;
</code></pre>
<p>"VLL"可以提前协议好是Vertical的LinearLayout，children就是子View的集合。</p>
<p>有了控件还需要一个页面承载，页面也能看成View，但是页面需要有更多的功能，全放View会导致View的属性过多，所以也能做一层抽象，</p>
<pre><code class="json">    &#123;
        "contextName": "home",
        "layout": &#123;
        
        &#125;
    &#125;
</code></pre>
<p>"contextName"能唯一标记一个页面，比如登录页面可以标记为"login"，"layout"实质就是一个View，字段和上面的基础控件一致。</p>
<p>有了上面的规则，现在可以尝试做一个有三个文本的首页：</p>
<pre><code class="json">    &#123;
        "contextName": "home",
        "layout": &#123;
            "name": "VLL",
            "children": [
                &#123;
                    "name": "TV",
                    "content": "打开页面",
                    "color": "#333333",
                    "size": "16"
                &#125;,
                &#123;
                    "name": "TV",
                    "content": "弹出Toast",
                    "color": "#333333",
                    "size": "16"
                &#125;,
                &#123;
                    "name": "TV",
                    "content": "请求网络",
                    "color": "#333333",
                    "size": "16"
                &#125;
            ]
        &#125;
    &#125;
</code></pre>
<h3>二、 View的响应</h3>
<p>第一步已经能自动填充控件了，但是如果真想点击第二个TextView去弹出一个Toast，怎么处理呢？可以尝试在View的数据里面指定一个动作：</p>
<pre><code class="json">    &#123;
         "name": "TV",
         "content": "弹出Toast",
         "color": "#333333",
         "size": "16",
         "action": &#123;
            "name": "toast",
            "msg": "弹出一下"
         &#125;
    &#125;
</code></pre>
<p>这样点击的时候就可以解析出一个Toast的动作。当然Action是需要提前穷举的，还是前面说的，一个App的动作肯定不是无限的。比如跳转一个页面：</p>
<pre><code class="json">    &#123;
         "name": "TV",
         "content": "打开页面",
         "color": "#333333",
         "size": "16",
         "action": &#123;
            "name": "open",
            "nextPage": &#123;
                "contextName": "detail",
                "layout": &#123;&#125;
            &#125;
         &#125;
    &#125;
</code></pre>
<p>"nextPage"已经能自动生成第二个页面了。甚至于，请求也是一个Action：</p>
<pre><code class="json">    &#123;
         "name": "TV",
         "content": "请求网络",
         "color": "#333333",
         "size": "16",
         "action": &#123;
            "name": "request",
            "url": "https://xxx.com",
            "params": &#123;
                "name": "rjp",
                "age": "18"
            &#125;
         &#125;
    &#125;
</code></pre>
<p>如果你已经封装了请求，上面的数据已经够去请求一下了，但是请求回来的数据呢？这就是说，有时候Action的动作是有后续动作的，有一种嵌套关系：</p>
<pre><code class="json">    &#123;
         "name": "TV",
         "content": "请求网络",
         "color": "#333333",
         "size": "16",
         "action": &#123;
            "name": "request",
            "url": "https://xxx.com",
            "params": &#123;
                "name": "rjp",
                "age": "18"
            &#125;,
            "action": "setData"
         &#125;
    &#125;
</code></pre>
<p>"request"的后续有一个"setData"的动作。这就不好处理了，因为每个页面的业务数据都是独特的，数据模型无法统一。所以需要一个中间层，能对后台下发的数据进行标准化输出：</p>
<pre><code class="java">    public class DataBean &#123;
        private String a;
        private String b;
        private String c;
        private String d;
        private String e;
        private String f;
        private String g;
    &#125;
</code></pre>
<p>也就是说，不管我请求哪个接口，返回的数据永远是abcdefg，我也不关心字段究竟代表什么。</p>
<p>那怎么知道下发的数据应该填充到哪个控件呢？可以通过给控件设置一个value，来指定需要的数据：</p>
<pre><code class="json">    &#123;
         "name": "TV",
         "content": "请求网络",
         "color": "#333333",
         "size": "16",
         "value": "a",
         "action": &#123;
            "name": "request",
            "url": "https://xxx.com",
            "params": &#123;
                "name": "rjp",
                "age": "18"
            &#125;,
            "action": "setData"
         &#125;
    &#125;
</code></pre>
<p>这样点击完请求数据，如果数据里面带上了"a": "后台数据"，就将数据填到这个TextView上。填充首先想到的就是遍历页面的根View，但是随着页面复杂化，非常耗时，可以参考局部刷新的做法，对有value属性的View进行缓存，只要遍历缓存集合就行了，非常高效。</p>
<h3>三、 拼多多</h3>
<p>说了这么多还没有一个完整的例子，下面一步步来实现。</p>
<pre><code class="java">    public class PageActivity extends AppCompatActivity implements IPage &#123;
    
        private List<View> viewCache;
    
        @Override
        protected void onCreate(Bundle savedInstanceState) &#123;
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_page);
    
            FrameLayout pageContainer = findViewById(R.id.page_container);
            Intent intent = getIntent();
            if (intent != null && intent.hasExtra("nextPage")) &#123;
                String nextPage = intent.getStringExtra("nextPage");
                PageBean pageBean = JSONObject.parseObject(nextPage, PageBean.class);
                if (pageBean != null) &#123;
                    viewCache = new ArrayList<>();
                    pageContainer.addView(LayoutFactory.createView(this, pageBean.getLayout()));
                &#125;
            &#125;
        &#125;
    
        @Override
        public Context getContext() &#123;
            return this;
        &#125;
    
        @Override
        public List<View> getViewCache() &#123;
            return viewCache;
        &#125;
    &#125;
</code></pre>
<p>创建一个简单的页面容器Activity，布局只有一个FrameLayout，从上一个页面接收json，这个json描述整个Page，当然也可以通过接口请求获取，测试阶段直接从Assets读取。</p>
<p>上面的关键是获取到json转成PageBean结构：</p>
<pre><code class="java">    public class PageBean &#123;
        private String contextName;
        private ViewBean layout;
    
        public ViewBean getLayout() &#123;
            return layout;
        &#125;
    
        public void setLayout(ViewBean layout) &#123;
            this.layout = layout;
        &#125;
    
        public String getContextName() &#123;
            return contextName;
        &#125;
    
        public void setContextName(String contextName) &#123;
            this.contextName = contextName;
        &#125;
    &#125;
</code></pre>
<p>ViewBean:</p>
<pre><code class="java">    public class ViewBean &#123;
    
        private String id;
        private String name;
        private String content;
        private String color;
        private String value;
        private float size = 14.0f;
        private int width;
        private int height;
        private List<ViewBean> children;
        private String action;
        private String url;
        private String itemType;
        
    &#125;
</code></pre>
<p>ViewBean存在一个问题就是所有的属性都糅合在一个数据结构里，会造成浪费，解决办法是一个类型的View给一个Bean，然后设置ViewType，但是那是优化时考虑的问题，目前只使用一个。</p>
<p>拿到了Layout就可以通过简单工厂模式开始渲染布局了：</p>
<pre><code class="java">    public class LayoutFactory &#123;
    
        public static View createView(IPage page, ViewBean viewBean) &#123;
            String name = viewBean.getName();
            switch (name) &#123;
                case ViewType.VLL:
                    return createLinearLayout(page, viewBean, true);
                case ViewType.HLL:
                    return createLinearLayout(page, viewBean, false);
                case ViewType.TV:
                    return createTextView(page, viewBean);
                case ViewType.IV:
                    return createImageView(page, viewBean);
                default:
                    return new View(page.getContext());
            &#125;
        &#125;
    
        private static View createLinearLayout(IPage page, ViewBean viewBean, boolean isVertical) &#123;
            LinearLayout vll = new LinearLayout(page.getContext());
            ViewGroup.LayoutParams layoutParams = new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT);
            vll.setLayoutParams(layoutParams);
            vll.setOrientation(isVertical ? LinearLayout.VERTICAL : LinearLayout.HORIZONTAL);
            List<ViewBean> children = viewBean.getChildren();
            if (children != null && children.size() > 0) &#123;
                int size = children.size();
                for (int i = 0; i < size; i++) &#123;
                    vll.addView(createView(page, children.get(i)));
                &#125;
            &#125;
            return vll;
        &#125;
        
        private static View createImageView(IPage page, ViewBean viewBean) &#123;
            ImageView imageView = new ImageView(page.getContext());
            imageView.setTag(R.id.image_tag_id, viewBean);
            ViewGroup.LayoutParams layoutParams = new ViewGroup.LayoutParams(viewBean.getWidth(), viewBean.getHeight());
            imageView.setLayoutParams(layoutParams);
            String url = viewBean.getUrl();
            if (!TextUtils.isEmpty(url)) &#123;
                Glide.with(page.getContext()).load(url).into(imageView);
            &#125;
            if (!TextUtils.isEmpty(viewBean.getValue())) &#123;
                List<View> viewCache = page.getViewCache();
                if (viewCache != null) &#123;
                    viewCache.add(imageView);
                &#125;
            &#125;
            return imageView;
        &#125;
    
        /**
         * 创建一个TextView
         *
         * @param page
         * @param viewBean
         * @return
         */
        private static View createTextView(IPage page, ViewBean viewBean) &#123;
            TextView tv = new TextView(page.getContext());
            try &#123;//多个try保证某一个脏数据不会导致view整体加载失败
                tv.setTextColor(Color.parseColor(viewBean.getColor()));
            &#125; catch (Exception e) &#123;
                e.printStackTrace();
                tv.setTextColor(Color.parseColor("#333333"));
            &#125;
            try &#123;
                tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, viewBean.getSize());
            &#125; catch (Exception e) &#123;
                e.printStackTrace();
                tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14.0f);
            &#125;
            if (!TextUtils.isEmpty(viewBean.getValue())) &#123;
                List<View> viewCache = page.getViewCache();
                if (viewCache != null) &#123;
                    viewCache.add(tv);
                &#125;
            &#125;
            tv.setText(viewBean.getContent());
            tv.setTag(viewBean);
            tv.setOnClickListener(v -> &#123;
                ViewBean bean = (ViewBean) v.getTag();
                IAction action = ActionFactory.createAction(page, bean.getAction());
                action.action(bean.getAction());
            &#125;);
            return tv;
        &#125;
    &#125;
</code></pre>
<p>注意填充的过程中判断value是否存在，存在直接存到viewCache集合里，后面设置数据能用上。</p>
<p>createView的方法传入了一个IPage接口，这个接口是为了方便获取context上下文和viewCache集合：</p>
<pre><code class="java">    public interface IPage &#123;
    
        Context getContext();
    
        List<View> getViewCache();
    &#125;
</code></pre>
<p>createTextView方法下设置了点击事件的监听，当点击的时候会触发Action，定义了IAction接口：</p>
<pre><code class="java">    public interface IAction &#123;
        void action(ActionBean action);
    &#125;
</code></pre>
<p>在点击的时候拿到action数据，通过ActionFactory简单工厂生成对应的Action实体，先看一个简单的Toast怎么实现：</p>
<pre><code class="java">    public class ToastAction implements IAction &#123;
    
        private IPage page;
    
        public ToastAction(IPage page) &#123;
            this.page = page;
        &#125;
    
        @Override
        public void action(ActionBean action) &#123;
            Toast.makeText(page.getContext(), action.getMsg(), Toast.LENGTH_SHORT).show();
        &#125;
    &#125;
</code></pre>
<p>这样整体App的Toast就都可以通过指定name = "toast"完成了。复杂一点的，比如请求Action之后，设置数据Action：</p>
<pre><code class="java">    public class RequestAction implements IAction &#123;
    
        private IPage page;
    
        public RequestAction(IPage page) &#123;
            this.page = page;
        &#125;
    
        @Override
        public void action(ActionBean action) &#123;
            if (action != null) &#123;
                try &#123;
                    Thread.sleep(2_000);
                &#125; catch (Exception e) &#123;
                    e.printStackTrace();
                &#125;
                String response = "&#123;\n" +
                        "      \"a\": \"这是通过请求获取的数据，真的！\"\n" +
                        "    &#125;";
                String lastAction = action.getAction();
                ActionBean lastActionBean = JSONObject.parseObject(lastAction, ActionBean.class);
                lastActionBean.setResponse(response);
                ActionFactory.createAction(page, lastAction).action(lastActionBean);
            &#125;
        &#125;
    &#125;
</code></pre>
<p>因为请求还要接入请求框架，直接模拟请求返回的数据了。执行设置数据Action的时候携带上请求回来的response：</p>
<pre><code class="java">    public class SetDataAction implements IAction &#123;
    
        private IPage page;
    
        public SetDataAction(IPage page) &#123;
            this.page = page;
        &#125;
    
        @Override
        public void action(ActionBean action) &#123;
            if (action != null) &#123;
                String response = action.getResponse();
                if (!TextUtils.isEmpty(response)) &#123;
                    DataBean dataBean = JSONObject.parseObject(response, DataBean.class);
                    List<View> viewCache = page.getViewCache();
                    if (viewCache != null && viewCache.size() > 0) &#123;
                        int size = viewCache.size();
                        for (int i = 0; i < size; i++) &#123;
                            View view = viewCache.get(i);
                            bindViewData(view, dataBean);
                        &#125;
                    &#125;
                &#125;
            &#125;
        &#125;
    
        /**
         * 绑定页面数据
         *
         * @param view
         * @param dataBean
         */
        private void bindViewData(View view, DataBean dataBean) &#123;
            if (view instanceof TextView) &#123;
                TextView textView = (TextView) view;
                ViewBean viewBean = (ViewBean) textView.getTag();
                String keyData = dataBean.getData(viewBean.getValue());
                textView.setText(keyData);
            &#125; else if (view instanceof ImageView) &#123;
                //TODO 
            &#125;
        &#125;
    &#125;
</code></pre>
<p>不需要反复遍历根节点，就能获取到设置了value = "a"的TextView，再拿到DataBean的a值，绑定上就可以看到结果了。</p>
<p>复杂的ListView绑定也是可以实现的。</p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Frjpacket%2FDSLDemo.git" target="_blank">Demo地址已更新</a></p>
  
</div>
            