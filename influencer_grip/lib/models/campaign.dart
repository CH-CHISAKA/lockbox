class Campaign {
  const Campaign({
    required this.id,
    required this.title,
    required this.brandName,
    required this.budget,
    required this.deadlineIso,
    required this.imageUrl,
    required this.tags,
    required this.description,
  });

  final String id;
  final String title;
  final String brandName;
  final double budget; // USD
  final String deadlineIso; // ISO8601
  final String imageUrl;
  final List<String> tags;
  final String description;
}
