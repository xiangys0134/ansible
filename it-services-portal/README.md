# IT服务门户网站

一个现代化的企业级IT服务门户网站，提供完整的IT服务申请和管理功能。

## 功能特点

### 🎯 核心功能
- **服务目录展示**: 清晰展示各类IT服务，包括基础设施、安全、技术支持和开发服务
- **智能搜索**: 支持服务名称和描述的实时搜索功能
- **分类筛选**: 按服务类别快速筛选相关服务
- **在线申请**: 一键申请各类IT服务，自动提交工单

### 🎨 用户体验
- **响应式设计**: 完美适配桌面、平板和移动设备
- **现代化UI**: 采用渐变色彩和卡片式设计，视觉效果佳
- **平滑动画**: 页面加载和交互动画，提升用户体验
- **快捷操作**: 支持键盘快捷键（Ctrl+K搜索、ESC清除）

### 📱 技术特性
- **纯前端实现**: HTML5 + CSS3 + JavaScript
- **无框架依赖**: 原生JavaScript实现，轻量高效
- **Font Awesome图标**: 丰富的图标库支持
- **CSS Grid布局**: 现代化的网格布局系统

## 文件结构

```
it-services-portal/
├── index.html          # 主页面文件
├── styles.css          # 样式文件
├── script.js           # JavaScript功能文件
└── README.md           # 项目说明文档
```

## 服务分类

### 🖥️ 基础设施服务
- **服务器申请**: 物理服务器和虚拟机资源申请
- **网络配置**: 网络端口、VLAN、防火墙配置
- **数据库服务**: MySQL、PostgreSQL、Oracle等数据库服务

### 🔒 安全服务
- **安全扫描**: 系统漏洞扫描和安全评估
- **权限管理**: 用户账号和访问权限管理
- **SSL证书**: HTTPS安全传输证书服务

### 🛠️ 技术支持
- **技术咨询**: 专业技术问题咨询和建议
- **故障排除**: 系统故障诊断和解决
- **性能监控**: 24/7系统性能监控服务

### 💻 开发服务
- **代码仓库**: Git代码仓库和CI/CD流水线
- **云平台服务**: 容器编排和微服务部署
- **环境配置**: 开发、测试、生产环境搭建

## 使用方法

### 1. 直接访问
在浏览器中打开 `index.html` 文件即可使用。

### 2. 本地服务器（推荐）
使用本地HTTP服务器运行，以获得更好的体验：

```bash
# 使用Python
python -m http.server 8000

# 或使用Node.js
npx http-server

# 或使用PHP
php -S localhost:8000
```

然后在浏览器中访问 `http://localhost:8000`

### 3. 功能使用
- **搜索服务**: 在搜索框中输入关键词
- **筛选服务**: 点击分类按钮筛选特定类型的服务
- **申请服务**: 点击"立即申请"按钮提交服务申请
- **快捷键**: 
  - `Ctrl+K` 或 `Cmd+K`: 快速聚焦搜索框
  - `ESC`: 清除搜索内容

## 自定义修改

### 添加新服务
在 `index.html` 中的 `services-grid` 部分添加新的服务卡片：

```html
<div class="service-card" data-category="your-category">
    <div class="service-icon">
        <i class="fas fa-your-icon"></i>
    </div>
    <div class="service-content">
        <h3>服务名称</h3>
        <p>服务描述</p>
        <div class="service-meta">
            <span class="service-time"><i class="fas fa-clock"></i> 处理时间</span>
            <span class="service-cost"><i class="fas fa-tag"></i> 费用</span>
        </div>
        <button class="btn-primary">立即申请</button>
    </div>
</div>
```

### 修改样式
编辑 `styles.css` 文件中的相应样式：

```css
/* 修改主题色彩 */
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --accent-color: #f5576c;
}
```

### 扩展功能
在 `script.js` 中添加新的JavaScript功能。

## 浏览器兼容性

- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+

## 最佳实践

1. **定期更新服务内容**: 保持服务信息的时效性
2. **优化搜索体验**: 根据用户搜索行为调整搜索建议
3. **监控申请流程**: 确保服务申请能够及时处理
4. **移动端优化**: 重点关注移动设备的使用体验

## 联系支持

- 📞 电话: 400-8888-8888
- 📧 邮箱: support@company.com
- 🕒 工作时间: 周一至周五 9:00-18:00
- 🆘 紧急支持: 24/7

## 许可证

本项目采用 MIT 许可证，详情请查看 LICENSE 文件。

---

© 2024 IT服务门户. 保留所有权利.