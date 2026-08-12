from core.config import load_sources


def main():
    sources = load_sources()

    print("CareerOS")
    print("========")
    print(f"Configured sources: {len(sources)}")

    for source in sources:
        status = "ENABLED" if source["enabled"] else "DISABLED"
        print(f"- {source['id']}: {status}")


if __name__ == "__main__":
    main()
