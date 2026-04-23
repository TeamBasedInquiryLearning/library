<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:import href="./core/pretext-latex.xsl" />


  <xsl:template match="titlepage-items">
    <xsl:text>[3\baselineskip]&#xa;</xsl:text>
    <xsl:apply-templates select="$bibinfo/author" mode="title-page"/>
    <xsl:text> \\&#xa;</xsl:text>
    <xsl:apply-templates select="$bibinfo/editor" mode="title-page" />
    <xsl:apply-templates select="$bibinfo/credit[title]" mode="title-page" />
  </xsl:template>

  <!--Authors on title page-->
  <xsl:template match="author|editor" mode="title-page">
      <xsl:text> {\Large </xsl:text>
      <xsl:apply-templates select="personname" />
      <xsl:if test="self::editor">
          <xsl:text>, </xsl:text>
          <xsl:apply-templates select="." mode="type-name"/>
      </xsl:if>
      <xsl:text>}  &#xa;</xsl:text>
      <xsl:if test="following-sibling::author">
          <xsl:text> \hspace{0.5in} &#xa;</xsl:text>
      </xsl:if>
  </xsl:template>

  <!--Contributing authors on title page-->
  <xsl:template match="credit" mode="title-page">
    <xsl:text>[3\baselineskip]&#xa;</xsl:text>
    <xsl:text>{\Large </xsl:text>
    <xsl:apply-templates  select="." mode="title-full" />
    <xsl:text>}\\[0.5\baselineskip]&#xa;</xsl:text>
    <xsl:for-each select="author">
        <xsl:text>{\normalsize </xsl:text>
        <xsl:apply-templates select="personname" />
        <xsl:text>}\\</xsl:text>
        <xsl:if test="following-sibling::author">
            <xsl:text>[0.5\baselineskip]&#xa;</xsl:text>
        </xsl:if>
        <xsl:text>&#xa;</xsl:text>
    </xsl:for-each>
  </xsl:template>


</xsl:stylesheet>