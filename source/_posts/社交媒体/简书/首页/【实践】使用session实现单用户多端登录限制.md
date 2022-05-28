
---
title: '【实践】使用session实现单用户多端登录限制'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1190574-cc54106d8bb1bd48.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1190574-cc54106d8bb1bd48.png'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1057" data-height="968"><img data-original-src="//upload-images.jianshu.io/upload_images/1190574-cc54106d8bb1bd48.png" data-original-width="1057" data-original-height="968" data-original-format="image/png" data-original-filesize="859079" src="https://upload-images.jianshu.io/upload_images/1190574-cc54106d8bb1bd48.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h1>1. 摘要</h1>
<p>软件设计中，经常存在这样的场景，为了防止计费等冲突限制，实现同一个用户不允许同一个用户多个设备同时登录，只允许唯一登录。本文介绍实现方法。</p>
<h1>2.设计场景</h1>
<p>1）同一时刻不允许某个用户多地登录。<br>
2）用户已在A处登录，现在从B处登录是允许的，但会把A处挤掉（考虑到用户在A处登录后因某些情况跑到了B处，但还想继续之前的工作，所以需要登录系统）。<br>
3）B处挤掉A后，A再做其它操作的时候系统会给出提示，该用户在别处登录，如不是本人操作可能密码泄漏，请修改密码。</p>
<h1>3. 业务流程图</h1>
<p>每个用户登录的时候，通常我们会将用户信息存入session，以便用户进行操作的时候系统方便得到用户的基本信息。但这个session具有私有性，只对当前用户可见（如果同意用户在不同浏览器登录会得到不同的session，这也是为什么可以多用户登录的根源所在）。那么接着问题就来了，某个用户登录的时候如何能知道自己是否在线，相信聪明的你已经想到，这还不好半，把在线的用户信息存储在一个公共的地方问题不就迎刃而解了么，网上一查，解决方案无出其右，大致为以下两种：<br>
　　1）数据库中标识在线用户<br>
　　2）存储到application中</p>
<p>经过重重考虑，我们会发现方案一需要解决许多棘手的问题（用户异常退出未来得及修改状态，频繁访问数据库影响性能等），这对于一个要求完美的你来说显然是不合时宜的，于是我们采用了方案二，将在线用户信息保存到application中，具体设计如下。</p>
<h2>3.1 登录流程图 -B处登录</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="441" data-height="521"><img data-original-src="//upload-images.jianshu.io/upload_images/1190574-016089a87690b9be.png" data-original-width="441" data-original-height="521" data-original-format="image/png" data-original-filesize="23103" src="https://upload-images.jianshu.io/upload_images/1190574-016089a87690b9be.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h2>3.1被挤掉后操作流程图 -A处已登录</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="607" data-height="498"><img data-original-src="//upload-images.jianshu.io/upload_images/1190574-b16b98f035381406.png" data-original-width="607" data-original-height="498" data-original-format="image/png" data-original-filesize="23385" src="https://upload-images.jianshu.io/upload_images/1190574-b16b98f035381406.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h1>3. 代码实现</h1>
<h4>1）登录方法</h4>
<pre><code>    @RequestMapping(value = "/login", method = RequestMethod.POST)
    public String login(String userName, String password, RedirectAttributes redirectAttributes, HttpServletRequest request) &#123;
        //判断用户是否已经在线及处理（已在线则剔除）
        String loginLimite = limiteLogin.loginLimite(request, userName);
        //判断用户名、密码是否正确
        String result = userService.login(userName, password);
        if (result.equals("success")) &#123;
            request.getSession().setAttribute("now_user", userService.findByUserName(userName));　　　　　　　　//用户掉线，登录后重定向到保存的链接
            Object url = request.getSession().getAttribute("redirect_link");
            if (url != null) &#123;
                request.getSession().removeAttribute("redirect_link");
                return "redirect:" + url.toString();
            &#125;
            return "index";
        &#125;
        redirectAttributes.addFlashAttribute("message", result);
        return "redirect:/other/toLogin";
    &#125;
</code></pre>
<h4>2）登录判断是否已经在线</h4>
<pre><code>@Service
@Transactional
public class LimiteLogin &#123;

    private static Logger log = Logger.getLogger(SessionListener.class);

    private static Map<String, String> loginUserMap = new HashMap<>();//存储在线用户
    private static Map<String, String> loginOutTime = new HashMap<>();//存储剔除用户时间
    @Autowired
    private UserService userService;

    public String loginLimite(HttpServletRequest request, String userName) &#123;
        User user = userService.findByUserName(userName);
        String sessionId = request.getSession().getId();
        for (String key : loginUserMap.keySet()) &#123;
            //用户已在另一处登录
            if (key.equals(user.getUserName()) && !loginUserMap.containsValue(sessionId)) &#123;
                log.info("用户：" + user.getUserName() + "，于" + DateUtil.dateFormat(new Date(), "yyyy-MM-dd HH:mm:ss") + "被剔除！");
                loginOutTime.put(user.getUserName(), DateUtil.dateFormat(new Date(), "yyyy-MM-dd HH:mm:ss"));
                loginUserMap.remove(user.getUserName());
                break;
            &#125;
        &#125;

        loginUserMap.put(user.getUserName(), sessionId);
        request.getSession().getServletContext().setAttribute("loginUserMap", loginUserMap);
        request.getSession().getServletContext().setAttribute("loginOutTime", loginOutTime);
        return "success";
    &#125;


&#125;
</code></pre>
<h4>3）登录拦截器（未登录跳转登录页）</h4>
<pre><code>public class LoginInterceptor extends HandlerInterceptorAdapter &#123;

    @Override
    public boolean preHandle(HttpServletRequest request,
                             HttpServletResponse response, Object handler) throws Exception &#123;
        HttpSession session = request.getSession();
        User user = (User) session.getAttribute("now_user");
        if (session.getAttribute("now_user") == null) &#123;
            response.sendRedirect(request.getContextPath() + "/other/toLogin");
            return false;
        &#125;

        //多用户登录限制判断,并给出提示信息
        boolean isLogin = false;
        if (user != null) &#123;
            Map<String, String> loginUserMap = (Map<String, String>) session.getServletContext().getAttribute("loginUserMap");
            String sessionId = session.getId();
            for (String key : loginUserMap.keySet()) &#123;
                //用户已在另一处登录
                if (key.equals(user.getUserName()) && !loginUserMap.containsValue(sessionId)) &#123;
                    isLogin = true;
                    break;
                &#125;
            &#125;
        &#125;
        if (isLogin) &#123;
            Map<String, String> loginOutTime = (Map<String, String>) session.getServletContext().getAttribute("loginOutTime");
            session.setAttribute("mess", "用户：" + user.getUserName() + "，于 " + loginOutTime.get(user.getUserName()) + " 已在别处登录!");
            loginOutTime.remove(user.getUserName());
            session.getServletContext().setAttribute("loginUserMap", loginOutTime);
            response.sendRedirect(request.getContextPath() + "/other/toLogin");
            return false;
        &#125;

        return super.preHandle(request, response, handler);
    &#125;

    @Override
    public void postHandle(HttpServletRequest request,
                           HttpServletResponse response, Object handler,
                           ModelAndView modelAndView) throws Exception &#123;
        super.postHandle(request, response, handler, modelAndView);
    &#125;

    @Override
    public void afterCompletion(HttpServletRequest request,
                                HttpServletResponse response, Object handler, Exception ex)
            throws Exception &#123;
        super.afterCompletion(request, response, handler, ex);
    &#125;
&#125;
</code></pre>
<h4>4）在session销毁的时候,把loginUserMap中保存的键值对清除</h4>
<pre><code>public class SessionListener implements HttpSessionListener &#123;

    private static Logger log = Logger.getLogger(SessionListener.class);

    @Override
    public void sessionCreated(HttpSessionEvent event) &#123;

    &#125;

    @Override
    public void sessionDestroyed(HttpSessionEvent event) &#123;
        HttpSession session = event.getSession();
        String sessionId = session.getId();
        //在session销毁的时候,把loginUserMap中保存的键值对清除
        User user = (User) session.getAttribute("now_user");
        if (user != null) &#123;
            Map<String, String> loginUserMap = (Map<String, String>) event.getSession().getServletContext().getAttribute("loginUserMap");
            if(loginUserMap.get(user.getUserName()).equals(sessionId))&#123;
                log.info("clean user from application : " + user.getUserName());
                loginUserMap.remove(user.getUserName());
                event.getSession().getServletContext().setAttribute("loginUserMap", loginUserMap);
            &#125;
        &#125;

    &#125;

&#125;
</code></pre>
<h4>5）web.xml</h4>
<pre><code><!-- session listener 多用户登录限制,退出清除session信息的同时清除application中存放用户登录信息-->
  <listener>
    <listener-class>com.service.limitelogin.SessionListener</listener-class>
  </listener>
</code></pre>
<h4>6）页面代码</h4>
<p>（用于给出提示的同时，清除被挤掉用户的session信息，否则提示信息会一直显示）</p>
<pre><code><script type="text/javascript">
    $(document).ready(function () &#123;
        var message='$&#123;mess&#125;';
        if (message != "") &#123;
            $.ajax(&#123;
                       type: 'GET',
                       async: false,
                       cache: false,
                       url: '/other/clearUserSession',
                       dataType: '',
                       data: &#123;&#125;,
                       success: function (data) &#123;
                       &#125;
                   &#125;);
            $('#mess').html(message);
        &#125;
    &#125;);
</script>
</code></pre>
<h4>7）清除挤掉用户session代码</h4>
<pre><code>/**
     * 多用户登录限制,清除session信息(登录信息、提示信息)
     *
     * @param request
     * @return
     */
    @ResponseBody
    @RequestMapping(value = "/clearUserSession")
    public String clearUserSession(HttpServletRequest request) &#123;
        HttpSession httpSession = request.getSession();
        //httpSession.invalidate();
        httpSession.removeAttribute("now_user");
        httpSession.removeAttribute("mess");
        return "success";
    &#125;
</code></pre>
<p>到此开发工作完成。</p>
<h4>8）运行结果</h4>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="698" data-height="115"><img data-original-src="//upload-images.jianshu.io/upload_images/1190574-ba114568d52338bd.png" data-original-width="698" data-original-height="115" data-original-format="image/png" data-original-filesize="7788" src="https://upload-images.jianshu.io/upload_images/1190574-ba114568d52338bd.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h1>4. 参考</h1>
<ol>
<li><p>代码下载：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fshaoyesun%2Flogin_limit" target="_blank">login_limit</a></p></li>
<li><p><a href="https://links.jianshu.com/go?to=http%3A%2F%2Fblog.csdn.net%2Fchenghui0317%2Farticle%2Fdetails%2F9373345" target="_blank">java web项目防止多用户重复登录解决方案</a></p></li>
<li><p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.cnblogs.com%2Fsunjf%2Fp%2Fmany_people_login_limite.html" target="_blank">多用户登录限制</a></p></li>
</ol>
  
</div>
            